import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import * as Highcharts from 'highcharts';
import { HighchartsChartModule } from 'highcharts-angular';
@Component({
  selector: 'app-predict-optimal',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule, HighchartsChartModule],
  templateUrl: './predict-optimal.component.html',
  styleUrls: ['./predict-optimal.component.css']
})
export class PredictOptimalComponent {
  date_str: string = '';
  date_fin: string = '';
  roomType: number = 168;
  occupancy: number = 0;


  results: any[] = [];
  loading: boolean = false;

  Highcharts: typeof Highcharts = Highcharts;
  chartOptions: Highcharts.Options = {};

  constructor(private http: HttpClient) {}

  predict() {
    const payload = {
      date_str: this.date_str,
      date_fin: this.date_fin,
      roomType: this.roomType,
      occupancy: this.occupancy
    };

    this.loading = true;

    this.http.post<any[]>('http://localhost:8000/predict/optimal', payload).subscribe({
      next: data => {
        this.results = data;
        this.generateChart(data);
        this.loading = false;
      },
      error: err => {
        console.error('Erreur API :', err);
        this.loading = false;
      }
    });
  }

  generateChart(data: any[]) {
    const categories = data.map(row => row.date);
    const availability = data.map(row => row.total_available);
    const avgPrice = data.map(row => row.mean_price_per_room);

    this.chartOptions = {
      chart: {
        type: 'column',     // you can also remove this as each series can have its own type
        zooming: {
          type: 'xy'
        }
      },
      title: {
        text: 'Availability vs Average Price per Room'
      },
      xAxis: [{
        categories: categories,
        crosshair: true
      }],
      yAxis: [
        { // Primary yAxis
          title: {
            text: 'Available Rooms',
            style: { color: '#7cb5ec' }
          }
        },
        { // Secondary yAxis
          title: {
            text: 'Average Price per Room',
            style: { color: '#434348' }
          },
          opposite: true
        }
      ],
      tooltip: {
        shared: true
      },
      series: [{
        name: 'Available Rooms',
        type: 'spline',
        yAxis: 0,
        data: availability,
        tooltip: { valueSuffix: ' rooms' }
      }, {
        name: 'Average Price per Room',
        type: 'spline',
        yAxis: 1,
        data: avgPrice,
        tooltip: { valueSuffix: 'MAD' }
      }]
    };

  }
}

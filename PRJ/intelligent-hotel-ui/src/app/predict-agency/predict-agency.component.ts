import { Component, importProvidersFrom } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-predict-agency',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './predict-agency.component.html',
  styleUrl: './predict-agency.component.css'
})
export class PredictAgency {
  agency_id: string = '';
  date_str: string = '';
  date_fin: string = '';
  roomType: number = 168;

  results: any[] = [];
  loading: boolean = false;

  constructor(private http: HttpClient) {}

  predict() {
    const payload = {
      date_str: this.date_str,
      date_fin: this.date_fin,
      roomType: this.roomType
    };
  const url = `http://localhost:8000/predict/agency/${this.agency_id}`;

  this.loading = true;
    this.http.post<any[]>(url, payload).subscribe({
      next: data => {
        this.results = data;
        this.loading = false;
      },
      error: err => {
        console.error('Erreur API :', err);
        this.loading = false;
      }
    });
  }
}
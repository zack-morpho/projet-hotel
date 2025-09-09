import { Component, importProvidersFrom } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-predict-total-available',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './predict-total-available.component.html',
styleUrls: ['./predict-total-available.component.css']})

export class PredictAvailabilityComponent {
  formData = {
    date_str: '',
    date_fin: '',
    roomType: 168
  };
  results: any[] = [];
  isLoading = false;

  constructor(private http: HttpClient) {}

  onSubmit() {
    this.isLoading = true;
    this.results = [];

    this.http.post<any[]>('http://localhost:8000/predict/availability', this.formData).subscribe({
      next: (response) => {
        this.results = response.map(item => ({
          date: item.date,
          total_available_predicted: item.total_available_predicted,
          iseventday: item.iseventday,
          vacance_MA: item.vacance_MA,
          roomType: item.roomType
        }));
        this.isLoading = false;
      },
      error: (error) => {
        console.error('Erreur lors de la prédiction', error);
        this.isLoading = false;
      }
    });
  }
}
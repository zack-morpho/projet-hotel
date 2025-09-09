import { Routes } from '@angular/router';
import { PredictAvailabilityComponent } from './predict-total-available/predict-total-available.component';
import { PredictOptimalComponent } from './predict-optimal/predict-optimal.component';
import { PredictAgency } from './predict-agency/predict-agency.component';
export const routes: Routes = [
  { path: '', redirectTo: 'predict-total-available', pathMatch: 'full' },
  { path: 'predict-total-available', component: PredictAvailabilityComponent },
  { path: 'predict-optimal', component: PredictOptimalComponent},
  { path: 'predict-agency', component: PredictAgency}

];

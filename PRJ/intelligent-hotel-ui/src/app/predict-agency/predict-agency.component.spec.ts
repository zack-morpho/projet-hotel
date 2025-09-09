import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictAgency } from './predict-agency.component';

describe('PredictAgency', () => {
  let component: PredictAgency;
  let fixture: ComponentFixture<PredictAgency>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PredictAgency]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PredictAgency);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

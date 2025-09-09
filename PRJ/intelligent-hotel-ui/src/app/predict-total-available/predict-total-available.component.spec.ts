import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictTotalAvailableComponent } from './predict-total-available.component';

describe('PredictTotalAvailable', () => {
  let component: PredictTotalAvailableComponent;
  let fixture: ComponentFixture<PredictTotalAvailableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PredictTotalAvailableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PredictTotalAvailableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

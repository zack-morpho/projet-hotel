import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictOptimalComponent} from './predict-optimal.component';

describe('PredictOptimal', () => {
  let component: PredictOptimalComponent;
  let fixture: ComponentFixture<PredictOptimalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PredictOptimalComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PredictOptimalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

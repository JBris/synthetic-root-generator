import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelOptimisationComponent } from './model-optimisation.component';

describe('ModelOptimisationComponent', () => {
  let component: ModelOptimisationComponent;
  let fixture: ComponentFixture<ModelOptimisationComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ModelOptimisationComponent]
    });
    fixture = TestBed.createComponent(ModelOptimisationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

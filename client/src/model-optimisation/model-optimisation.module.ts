import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ModelOptimisationRoutingModule } from './model-optimisation-routing.module';
import { ModelOptimisationComponent } from './model-optimisation.component';


@NgModule({
  declarations: [
    ModelOptimisationComponent
  ],
  imports: [
    CommonModule,
    ModelOptimisationRoutingModule
  ]
})
export class ModelOptimisationModule { }

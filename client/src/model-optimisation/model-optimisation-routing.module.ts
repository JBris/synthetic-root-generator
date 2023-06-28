import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ModelOptimisationComponent } from './model-optimisation.component';

const routes: Routes = [{ path: '', component: ModelOptimisationComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ModelOptimisationRoutingModule { }

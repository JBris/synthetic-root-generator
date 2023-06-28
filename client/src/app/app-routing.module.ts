import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [ 
  { 
    path: 'model-optimisation', 
    loadChildren: () => import('../model-optimisation/model-optimisation.module').then(m => m.ModelOptimisationModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

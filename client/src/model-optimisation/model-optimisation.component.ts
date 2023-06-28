import { Component, OnInit } from '@angular/core';
import { Apollo, gql } from 'apollo-angular';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';

const QUERY = gql`
query optimiseModel($a: Int!, $b: Int!) {
	optimiseModel(a: $a, b: $b)
}
`;

@Component({
  selector: 'app-model-optimisation',
  templateUrl: './model-optimisation.component.html',
  styleUrls: ['./model-optimisation.component.sass']
})
export class ModelOptimisationComponent implements OnInit {
  optimiseModel?: Observable<any>;
  loading = true;
  error: any;

  constructor(private apollo: Apollo) {}
 
  ngOnInit() {    
    this.optimiseModel = this.apollo
      .watchQuery({
        query: QUERY,
        variables: { a: 1, b: 2 }
      })
      .valueChanges.pipe(
        map((result: any) => result.data && result.data.optimiseModel),
        catchError((err) => err)
      )
  }
}

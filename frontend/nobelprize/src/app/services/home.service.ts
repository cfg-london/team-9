import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';

import { ConceptNode } from '../models/concept-node';

@Injectable()
export class HomeService {
  constructor(private http: HttpClient) { }

  getConceptNodes(): Observable<ConceptNode[]> {
    return new Observable((observer) => {
      observer.next([
        {id: 1, label: 'bla1'},
        {id: 2, label: 'bla2'}
      ]);
      observer.complete();
  });
  }
}

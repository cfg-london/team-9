import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { map } from 'rxjs/operators';

@Injectable()
export class HomeService {
  constructor(private http: HttpClient) { }

  getConceptNodes(size: number): Observable<any[]> {
    return new Observable((observer) => {
      observer.next([
        {
          id: 1,
          label: 'bla1',
          size: 40,
          type: 'laureate',
          conceptId: '1'
        },
        {id: 2, label: 'bla2', size: 20, type: 'prize', conceptId: '1'}
      ]);
      observer.complete();
  }).pipe(
    map((resp: any[]) => resp.map(elem => {
      elem.font = {size: elem.size};
      return elem;
    }))
  );
  }
}

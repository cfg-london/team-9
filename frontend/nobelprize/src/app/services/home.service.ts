import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { map } from 'rxjs/operators';

@Injectable()
export class HomeService {
  constructor(private http: HttpClient) { }

  getConceptNodes(size: number): Observable<any[]> {
    return this.http.get(`http://localhost:5000/laureate/graph/id/1/limit/${size}`)
        .pipe(
          map((resp: any[]) => {
            console.log(resp);
            resp[0] = resp[0].map(elem => {
              elem.font = {size: elem.size};
              return elem;
            });
            return resp;
          }));
  }
}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { map } from 'rxjs/operators';

@Injectable()
export class HomeService {
  constructor(private http: HttpClient) { }

  getConceptNodes(size: number): Observable<any[]> {
    return this.http.get(`http://52.214.137.161:5000/homepage_graph  `)
        .pipe(
          map((resp: any) => {
            resp.nodes = resp.nodes.map(elem => {
              elem.font = {size: elem.score ? elem.score / 10 : 15};
              if (elem.type !== 'laureate') {
                elem.color = {background: '#FFA000'};
              }
              return elem;
            });

            return resp;
          }));
  }
}

import { Injectable } from '@angular/core';

import { Observable } from 'rxjs/Observable';

import { Laureate } from '../models/laureate';

import {HttpClient} from '@angular/common/http';

@Injectable()
export class LaureatesService {
  laureate: any;

  constructor(private http: HttpClient) { }

  getLaureateById(id: number): Observable<Laureate> {
    return this.http.get<Laureate>('http://localhost:5000/laureate/id/' + id);
  }
}

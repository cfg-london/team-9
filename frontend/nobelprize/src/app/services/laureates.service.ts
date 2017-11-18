import { Injectable } from '@angular/core';

import { Observable } from 'rxjs/Observable';

import { Laureate } from '../models/laureate';

import {HttpClient} from '@angular/common/http';

@Injectable()
export class LaureatesService {
  laureate: any;

  constructor(private http: HttpClient) { }

  getLaureateById(id: number): Observable<Laureate> {
    return this.http.get<Laureate>('http://52.214.137.161:5000/laureate/id/' + id);
  }

  getNeighbours(id: number, limit: number): Observable<any[]> {
    return this.http.get<any[]>(`http://52.214.137.161:5000/laureate/neighbours/id/${id}/limit/${limit}`);
  }

  getRelevantLinks(text: string): Observable<any[]> {
    return this.http.get<any[]>(`http://52.214.137.161:5000/laureate/relevant_links`);
  }
}

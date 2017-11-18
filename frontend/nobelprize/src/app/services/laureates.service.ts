import { Injectable } from '@angular/core';

import { Observable } from 'rxjs/Observable';

import { Laureate } from '../models/laureate';

import {HttpClient} from '@angular/common/http';

@Injectable()
export class LaureatesService {
  laureate: string;

  constructor(private http: HttpClient) { }

  getLaureateById(id: number): Observable<Laureate> {
    this.http.get('http://localhost:5000/laureate/id/' + id).subscribe(response => {
      this.laureate = response['results'];
    });



    const default_laureate = {name: 'andrei', description:
      'The growth, division, and death of living cells are regulated by their genes. ' +
      'If these functions are out of balance, tumors can form. One reason for this may be the incorporation of ' +
      'virus genes into the genes of host cells. Harald zur Hausen demonstrated in 1983 that cervical cancer in ' +
      'humans is caused by certain types of papilloma viruses (wart viruses), the genes from which are incorporated ' +
      'into the host cells\' DNA. This discovery made it possible to develop a vaccine against cervical cancer, ' +
      'which had been the second most common tumor disease in women.'};

    return new Observable(observer => {
      observer.next(default_laureate);
    });
  }
}

import { Injectable } from '@angular/core';

import { Observable } from 'rxjs/Observable';

import { Laureate } from '../models/laureate';

@Injectable()
export class LaureatesService {

  constructor() { }

  getLaureateById(id: number): Observable<Laureate> {
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

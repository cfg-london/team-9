import { Injectable } from '@angular/core';

@Injectable()
export class LaureatesService {

  constructor() { }

  getLaureateById(id: number) {
    const default_laureate = {name: 'andrei'};

    return default_laureate
  }
}

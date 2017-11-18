import { TestBed, inject } from '@angular/core/testing';

import { LaureatesService } from './laureates.service';

describe('LaureatesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [LaureatesService]
    });
  });

  it('should be created', inject([LaureatesService], (service: LaureatesService) => {
    expect(service).toBeTruthy();
  }));
});

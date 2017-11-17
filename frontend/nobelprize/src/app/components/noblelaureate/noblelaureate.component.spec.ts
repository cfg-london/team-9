import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NoblelaureateComponent } from './noblelaureate.component';

describe('NoblelaureateComponent', () => {
  let component: NoblelaureateComponent;
  let fixture: ComponentFixture<NoblelaureateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NoblelaureateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NoblelaureateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

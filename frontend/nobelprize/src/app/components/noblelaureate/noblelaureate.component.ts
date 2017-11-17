import { Component, OnInit, Input } from '@angular/core';
import { Laureate } from '../../models/laureate';

@Component({
  selector: 'app-noblelaureate',
  templateUrl: './noblelaureate.component.html',
  styleUrls: ['./noblelaureate.component.css']
})
export class NoblelaureateComponent implements OnInit {
  @Input() laurate: Laureate;

  constructor() { }

  ngOnInit() {
  }

}

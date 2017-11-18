import { Component, Input, OnInit } from '@angular/core';
import { Prize } from "../../models/prize";

@Component({
  selector: 'app-prize',
  templateUrl: './prize.component.html',
  styleUrls: ['./prize.component.scss']
})
export class PrizeComponent implements OnInit {
  @Input() prize: Prize;

  constructor() { }

  ngOnInit() {
  }
}

import {Component, Input, OnInit} from '@angular/core';
import {Affiliation} from "../../models/affiliation";

@Component({
  selector: 'app-affiliation',
  templateUrl: './affiliation.component.html',
  styleUrls: ['./affiliation.component.scss']
})
export class AffiliationComponent implements OnInit {
  @Input() affiliation: Affiliation;

  constructor() { }

  ngOnInit() {
  }
}

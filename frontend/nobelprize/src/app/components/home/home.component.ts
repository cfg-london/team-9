import { Component, OnInit } from '@angular/core';
import { Node, Network, DataSet } from 'vis';

import { HomeService } from '../../services/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  network: Network;

  constructor(private homeService: HomeService) { }

  ngOnInit() {
    const dataOptions = {};
    const data: DataSet<any> = new DataSet(dataOptions);
    this.homeService.getConceptNodes().subscribe(resp => {
      data.add(resp);
    });
    const options = {
    };

    this.network = new Network(document.getElementById('vis-network'), {nodes: data}, options);
  }
}

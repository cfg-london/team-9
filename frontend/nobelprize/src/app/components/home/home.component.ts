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
  viewDataSet: DataSet<any>;
  data: DataSet<any>;
  searchParameter: string;

  constructor(private homeService: HomeService) { }

  ngOnInit() {
    const dataOptions = {};
    this.data = new DataSet(dataOptions);
    this.homeService.getConceptNodes(10).subscribe(resp => {
      this.data.add(resp);
    });
    this.viewDataSet = this.data;

    const options = {};

    this.network = new Network(document.getElementById('vis-network'), {nodes: this.viewDataSet}, options);
    this.network.on('click', (event) => {
      // redirect to page
    });
  }

  // filterNodes() {
  //   this.viewDataSet = this.filterData(this.data, this.searchParameter);
  // }

  // private filterData(data: DataSet<any>, searchParameter: string): DataSet<any> {
  //   return new DataSet<any>(data.get({filter: elem => elem.label.indexOf(searchParameter) > -1}));
  // }
}

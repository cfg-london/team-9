import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Node, Network, DataSet } from 'vis';

import { HomeService } from '../../services/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  network: Network;
  searchParameter: string;
  graphData;

  constructor(private homeService: HomeService,
              private router: Router) { }

  ngOnInit() {
    this.homeService.getConceptNodes(5).subscribe((resp: any) => {
      const dataOptions = {};
      const data = new DataSet(dataOptions);
      data.add(resp.nodes);
      this.graphData = {
        edges: resp.edges,
        nodes: data
      };

      const options = {
        nodes: {
          color: {
            background: 'rgb(63, 81, 181)'
          },
          font: {
            color: 'white',
            face: 'Roboto'
          },
          margin: 100
        },
        edges: {
          length: 200
        }
      };

      this.network = new Network(document.getElementById('vis-network'), this.graphData, options);
      this.network.on('click', (event) => {
        // redirect to page
        if (event.nodes.length >= 1) {
          const node = this.graphData.nodes.get(event.nodes[0]) as any;
          this.router.navigate([`/${node.type}/${node.value.id}`]);
        }
      });
    });
  }

  // filterNodes() {
  //   this.viewDataSet = this.filterData(this.data, this.searchParameter);
  // }

  // private filterData(data: DataSet<any>, searchParameter: string): DataSet<any> {
  //   return new DataSet<any>(data.get({filter: elem => elem.label.indexOf(searchParameter) > -1}));
  // }
}

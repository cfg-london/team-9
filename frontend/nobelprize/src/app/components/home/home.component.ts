import { Component, OnInit, ElementRef } from '@angular/core';
import { Node, Network, DataSet } from 'vis';

interface ContentNode {
  id: number;
  label: string;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  network: Network;

  constructor(private element: ElementRef) { }

  ngOnInit() {
    const dataOptions = {};
    const data: DataSet<ContentNode> = new DataSet(dataOptions);
    data.add([
      {id: 1, label: 'bla1'},
      {id: 2, label: 'bla2'}
    ]);
    const options = {};

    this.network = new Network(document.getElementById('vis-network'), {nodes: data}, options);

  }

}

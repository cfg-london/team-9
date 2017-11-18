import { Component, OnInit, Input } from '@angular/core';
import { Laureate } from '../../models/laureate';
import { LaureatesService } from '../../services/laureates.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-noblelaureate',
  templateUrl: './noblelaureate.component.html',
  styleUrls: ['./noblelaureate.component.scss']
})
export class NoblelaureateComponent implements OnInit {
  private sub: any;
  id: number;
  laureate: Laureate;
  recomandations: any[];
  relevantlinks: any[];

  constructor(private laureatesService: LaureatesService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
      this.id = +params['id'];
    });

    this.laureatesService.getLaureateById(this.id).subscribe(response => {
      this.laureate = response;

      this.laureatesService.getRelevantLinks(this.id, this.laureate.value.prizes[0].motivation).subscribe(response => {
        this.relevantlinks = response;
        console.log(response);
      });
    });

    this.laureatesService.getNeighbours(this.id, 10).subscribe(response => {
      this.recomandations = response;
    });
  }

}

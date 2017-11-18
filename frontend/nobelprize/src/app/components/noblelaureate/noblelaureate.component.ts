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
  einsteinWork = 'If metal electrodes are exposed to light, electrical sparks between them occur more readily. For this "photoelectric effect" to occur, the light waves must be above a certain frequency, however. According to physics theory, the light\'s intensity should be critical. In one of several epoch-making studies beginning in 1905, Albert Einstein explained that light consists of quanta - "packets" with fixed energies corresponding to certain frequencies. One such light quantum, a photon, must have a certain minimum frequency before it can liberate an electron.'

  constructor(private laureatesService: LaureatesService, private route: ActivatedRoute) {}

  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
      this.id = +params['id'];
      this.laureatesService.getLaureateById(this.id).subscribe(response => {
        this.laureate = response;

        this.laureatesService.getRelevantLinks(this.id, this.laureate.value.born).subscribe(response => {
          this.relevantlinks = response;
          console.log(response);
        });
      });

      this.laureatesService.getNeighbours(this.id, 10).subscribe(response => {
        this.recomandations = response;
      });
    });
  }

}

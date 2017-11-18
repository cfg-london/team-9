import {Affiliation} from "./affiliation";

export interface Prize {
  affiliations: Affiliation[];
  category: string;
  motivation: string;
  share: string;
  year: string;
}

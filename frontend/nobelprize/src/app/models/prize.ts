import {Affiliation} from "./affiliation";

export interface Prize {
  affiliations: Affiliation[];
  category: String;
  motivation: String;
  share: String;
  year: String;
}

import {Prizes} from "./prizes";

export interface Laureate {
  born: string;
  bornCity: string;
  bornCountry: string;
  bornCountryCode: string;
  died: string;
  diedCity: string;
  diedCountry: string;
  diedCountryCode: string;
  firstname: string;
  gender: string;
  id: string;
  surname: string;
  prizes: Prizes[];
}

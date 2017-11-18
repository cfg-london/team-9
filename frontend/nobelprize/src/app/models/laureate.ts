import {Prize} from "./prize";

export interface Laureate {
  id: string;
  type:string;
  value: {
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
    surname: string;
    prizes: Prize[];
  }
}

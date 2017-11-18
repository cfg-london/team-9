import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { NoblelaureateComponent } from './components/noblelaureate/noblelaureate.component';
import {LaureatesService} from "./services/laureates.service";


@NgModule({
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  declarations: [
    AppComponent,
    HomeComponent,
    NoblelaureateComponent
  ],
  providers: [
    LaureatesService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

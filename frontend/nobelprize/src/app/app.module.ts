import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';

import { HomeService } from './services/home.service';

import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { NoblelaureateComponent } from './components/noblelaureate/noblelaureate.component';
import {LaureatesService} from './services/laureates.service';


@NgModule({
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  declarations: [
    AppComponent,
    HomeComponent,
    NoblelaureateComponent
  ],
  providers: [
    HomeService,
    LaureatesService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

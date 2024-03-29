import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';

import { AppRoutingModule } from './app-routing.module';

import { HomeService } from './services/home.service';

import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { NoblelaureateComponent } from './components/noblelaureate/noblelaureate.component';
import { LaureatesService } from './services/laureates.service';
import { PrizeComponent } from "./components/prize/prize.component";
import { AffiliationComponent } from './components/affiliation/affiliation.component';


@NgModule({
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AppRoutingModule,
    MatToolbarModule,
    MatInputModule,
    MatButtonModule
  ],
  declarations: [
    AppComponent,
    HomeComponent,
    NoblelaureateComponent,
    PrizeComponent,
    AffiliationComponent
  ],
  providers: [
    HomeService,
    LaureatesService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

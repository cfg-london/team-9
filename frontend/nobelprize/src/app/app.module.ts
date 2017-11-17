import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { NoblelaureateComponent } from './components/noblelaureate/noblelaureate.component';


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
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

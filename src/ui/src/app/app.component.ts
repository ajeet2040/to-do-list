import { Component, OnInit } from '@angular/core';
import { TokenStorageService } from './_services/token-storage.service';
import {Router} from '@angular/router';
import { AuthService } from './_services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  private roles: string[] = [];
  isLoggedIn = false;
  username?: string;
  errorMessage = '';


  constructor(private tokenStorageService: TokenStorageService, private router: Router,
      private authService: AuthService
    ) { }

  ngOnInit(): void {
    this.isLoggedIn = !!this.tokenStorageService.getToken();

    if (this.isLoggedIn) {
      const user = this.tokenStorageService.getUser();
      this.username = user.username;
      this.router.navigate(['/'])
    }
    else{
      this.router.navigate(['/login'])
    }
  }

  logout(): void {
    this.tokenStorageService.signOut();
    window.location.reload();
  }
}
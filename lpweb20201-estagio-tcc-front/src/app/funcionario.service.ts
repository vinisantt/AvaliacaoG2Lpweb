import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environments/environment';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root',
})
export class FuncionarioService {
  constructor(private http: HttpClient, private auth$: AuthService) {}

  lista() {
    return this.http.get(
      environment.API_URL.concat('funcionarios/'),
      this.auth$.httpOptions()
    );
  }
}

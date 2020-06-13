import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environments/environment';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root',
})
export class ProfessorService {
  constructor(private http: HttpClient, private auth$: AuthService) {}

  lista() {
    return this.http.get(
      environment.API_URL.concat('professores/'),
      this.auth$.httpOptions()
    );
  }

  cadastrar(curso_id: number, funcionario_id: number, funcao: string) {
    return this.http.post(
      environment.API_URL.concat('professores/'),
      {
        curso_id: curso_id,
        funcionario_id: funcionario_id,
        funcao: funcao,
      },
      this.auth$.httpOptions()
    );
  }

  excluir(id: number) {
    return this.http.delete(
      environment.API_URL.concat(`professores/${id}/`),
      this.auth$.httpOptions()
    );
  }
}

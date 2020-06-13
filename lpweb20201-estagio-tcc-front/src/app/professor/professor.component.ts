import { Component, OnInit } from '@angular/core';
import { ProfessorService } from '../professor.service';

@Component({
  selector: 'app-professor',
  templateUrl: './professor.component.html',
  styleUrls: ['./professor.component.css'],
})
export class ProfessorComponent implements OnInit {
  constructor(private profService$: ProfessorService) {}

  professores: Array<any> = [];

  erro: any = { erro: false, id: null };

  ngOnInit(): void {
    this.profService$.lista().subscribe((dados: any) => {
      for (let result of dados.results) {
        if (result.funcao == 'coordenador-estagio-tcc') {
          result.funcao = 'Coordenador de Estágio e TCC';
        } else if (result.funcao == 'professor') {
          result.funcao = 'Professor';
        } else {
          result.funcao = 'Coordenador';
        }
        this.professores.push(result);
      }
    });
  }

  atualiza() {
    this.profService$.lista().subscribe((dados: any) => {
      this.professores = dados.results;
    });
  }

  excluir(id: number) {
    this.profService$.excluir(id).subscribe(
      (dados) => {
        this.erro = { erro: false, id: id };
        this.atualiza();
      },
      (error) => {
        this.erro = { erro: true, id: id };
      }
    );
  }
}

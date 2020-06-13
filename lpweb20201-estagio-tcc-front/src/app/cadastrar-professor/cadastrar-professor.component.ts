import { Component, OnInit } from '@angular/core';
import { CursoService } from '../curso.service';
import { FuncionarioService } from '../funcionario.service';
import { ProfessorService } from '../professor.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cadastrar-professor',
  templateUrl: './cadastrar-professor.component.html',
  styleUrls: ['./cadastrar-professor.component.css'],
})
export class CadastrarProfessorComponent implements OnInit {
  constructor(
    private c$: CursoService,
    private f$: FuncionarioService,
    private p$: ProfessorService,
    private router: Router
  ) {}

  cursos: Array<any> = [];
  curso: any;
  funcionarios: Array<any> = [];
  funcionario: any = null;
  funcoes: Array<any> = [
    { func: 'coordenador', string: 'Coordenador' },
    { func: 'coordenador-estagio-tcc', string: 'Coordenador de Estágio e TCC' },
    { func: 'professor', string: 'Professor' },
  ];
  funcao: any = null;
  erro: any = { erro: false, local: null, submitado: false };

  ngOnInit(): void {
    this.c$.lista().subscribe((dados: any) => (this.cursos = dados.results));
    this.f$
      .lista()
      .subscribe((dados: any) => (this.funcionarios = dados.results));
  }

  salvar() {
    this.p$.cadastrar(this.curso, this.funcionario, this.funcao).subscribe(
      (dados) => {
        setTimeout(() => {
          this.router.navigate(['professores']);
        }, 5000);
        this.erro = { erro: false, submitado: true };
      },
      (error) => {
        console.log(error);
        this.erro = {
          erro: true,
          status: error.status,
          local: error.error,
          submitado: true,
        };
      }
    );
  }
}

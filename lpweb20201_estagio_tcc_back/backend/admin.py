from django.contrib import admin
from .models import *

admin.site.register(Perfil)
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(AlunoUsuario)
admin.site.register(Matricula)
admin.site.register(Funcionario)
admin.site.register(FuncionarioUsuario)
admin.site.register(Professor)
admin.site.register(ColaboradorExterno)
admin.site.register(ColaboradorExternoUsuario)
admin.site.register(Orientacao)
admin.site.register(PropostaDeEstagio)
admin.site.register(PropostaDeTCC)
admin.site.register(MembroDeBancaDeProposta)
admin.site.register(AvaliacaoDeProposta)

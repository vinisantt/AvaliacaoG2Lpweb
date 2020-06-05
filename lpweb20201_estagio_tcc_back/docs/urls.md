# URLs

Utilizando o recurso de *rotas* do DRF (django rest framework) são declaradas as seguintes rotas, associadas às suas [views](views.md) respectivas:

| caminho                        | view                          |
| :----------------------------- | :---------------------------- |
| `api/users/`                   | `UserViewSet`                 |
| `api/groups/`                  | `GroupViewSet`                |
| `api/perfil-logado/`           | `PerfilLogadoViewSet`         |
| `api/perfis/`                  | `PerfilViewSet`               |
| `api/usuario-logado/`          | `UsuarioLogadoDetailsViewSet` |
| `api/cursos/`                  | `CursoViewSet`                |
| `api/alunos/`                  | `AlunoViewSet`                |
| `api/matriculas/`              | `MatriculaViewSet`            |
| `api/funcionarios/`            | `FuncionarioViewSet`          |
| `api/professores/`             | `ProfessorViewSet`            |
| `api/orientacoes/`             | `OrientacaoViewSet`           |
| `api/propostas-de-estagio/`    | `PropostaDeEstagioViewSet`    |
| `api/propostas-de-tcc/`        | `PropostaDeTCCViewSet`        |
| `api/avaliacoes-de-propostas/` | `AvaliacaoDePropostaViewSet`  |
| `api/colaboradores-externos/`  | `ColaboradorExternoViewSet`   |

Além dessas rotas estão disponíveis:

| caminho              | descrição ou view                                         |
| :------------------- | :-------------------------------------------------------- |
| `admin/`             | conjunto de URLs do **django admin**                      |
| `api/auth/`          | conjunto de URLs do **rest_framework**, para autenticação |
| `api/token-auth/`    | view `obtain_jwt_token`                                   |
| `api/token-refresh/` | view `refresh_jwt_token`                                  |

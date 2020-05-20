# URLs

Utilizando o recurso de *rotas* do DRF (django rest framework) são declaradas as seguintes rotas:

| caminho              | view                  |
| :------------------- | :-------------------- |
| `api/users/`         | `UserViewSet`         |
| `api/groups/`        | `GroupViewSet`        |
| `api/perfil-logado/` | `PerfilLogadoViewSet` |
| `api/perfis/`        | `PerfilViewSet`       |

Além dessas rotas estão disponíveis:

| caminho            | descrição ou view                                         |
| :----------------- | :-------------------------------------------------------- |
| `admin/`           | conjunto de URLs do **django admin**                      |
| `api/auth/`        | conjunto de URLs do **rest_framework**, para autenticação |
| `api/token-auth/`    | view `obtain_jwt_token`                                   |
| `api/token-refresh/` | view `refresh_jwt_token`                                  |

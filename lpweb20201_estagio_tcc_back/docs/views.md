# Views

## `UserViewSet`

A view `UserViewSet` fornece funcionalidades para gerenciar os dados de usuário. Possui os campos:

* `queryset`: associado à lista dos usuários, ordenada de forma decrescente pelo campo `date_joined`
* `serializer_class`: indica que a classe utilizada na serialização é `UserSerializer`
* `permission_classes`: indica somente o usuário autenticado tem acesso à view

## `GroupViewSet`

A view `GroupViewSet` fornece funcionalidades para gerenciar os dados de grupos de usuários. Possui os campos:

* `queryset`: associado à lista dos grupos
* `serializer_class`: indica que a classe utilizada na serialização é `GroupSerializer`
* `permission_classes`: indica somente o usuário autenticado tem acesso à view

## `PerfilLogadoViewSet`

A view `PerfilLogadoViewSet` permite apenas acesso de leitura do perfil associado ao usuário da requisião (se disponível). Possui os campos:

* `serializer_class`: indica que a classe utilizada na serialização é `PerfilSerializer`
* `permission_classes`: indica somente o usuário autenticado tem acesso à view

Além disso, contém os métodos:

* `get_queryset`: utilizado para filtrar o model `Perfil`, retornando apenas o perfil do usuário da requisição (`request.user`)
* `list`: utiliza o método `get_queryset()` para obter o perfil do usuário e, se existir, utiliza o `PerfilSerializer` para compor a resposta da requisição; caso contrário, o retorno é vazio e com código **404**, para indicar que o perfil não foi encontrado (usuário não possui perfil)

## `PerfilViewSet`

A view `PerfilViewSet` fornece funcionalidades para gerenciar os dados de perfis de usuários. Possui os campos:

* `queryset`: associado à lista dos perfis de usuários
* `serializer_class`: indica que a classe utilizada na serialização é `PerfilSerializer`
* `permission_classes`: indica somente o usuário autenticado tem acesso à view


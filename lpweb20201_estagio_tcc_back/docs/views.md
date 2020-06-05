# Views <!-- omit in toc -->

- [`UserViewSet`](#userviewset)
- [`GroupViewSet`](#groupviewset)
- [`UsuarioLogadoViewSet`](#usuariologadoviewset)
- [`PerfilLogadoViewSet`](#perfillogadoviewset)
- [`PerfilViewSet`](#perfilviewset)
- [`CursoViewSet`](#cursoviewset)
- [`AlunoViewSet`](#alunoviewset)
- [`MatriculaViewSet`](#matriculaviewset)
- [`FuncionarioViewSet`](#funcionarioviewset)
- [`ProfessorViewSet`](#professorviewset)
- [`OrientacaoViewSet`](#orientacaoviewset)
- [`PropostaDeEstagioViewSet`](#propostadeestagioviewset)
- [`PropostaDeTCCViewSet`](#propostadetccviewset)
- [`AvaliacaoDePropostaViewSet`](#avaliacaodepropostaviewset)
- [`ColaboradorExternoViewSet`](#colaboradorexternoviewset)

## `UserViewSet`

A view `UserViewSet` fornece funcionalidades para gerenciar os dados de usuário. Possui os campos:

- `queryset`: associado à lista dos usuários, ordenada de forma decrescente pelo campo `date_joined`
- `serializer_class`: indica que a classe utilizada na serialização é `UserSerializer`
- `permission_classes`: indica somente o usuário admin tem acesso à view
- `search_fields`: indica que a lista dos usuários pode ser pesquisada conforme o parâmetro de URL `search`, com base nos valores dos campos `username` e `email`
- `ordering_fields`: indica que a lista dos usuários pode ser ordenada conforme o parâmetro de URL `ordering`, de forma crescente e decrescente, considerando os campos: `id`, `username`, `email`

## `GroupViewSet`

A view `GroupViewSet` fornece funcionalidades para gerenciar os dados de grupos de usuários. Possui os campos:

- `queryset`: associado à lista dos grupos
- `serializer_class`: indica que a classe utilizada na serialização é `GroupSerializer`
- `permission_classes`: indica somente o usuário admin tem acesso à view

## `UsuarioLogadoViewSet`

A view `UsuarioLogadoViewSet` permite acesso de leitura dos detalhes do usuário da requisição. Possui os campos:

- `serializer_class`: indica que a classe utilizada na serialização é `UsuarioDetalhadoSerializer`
- `permission_classes`: indica que somente um usuário autenticado tem acesso à view

Além disso, contém os métodos:

- `get_queryset`: utilizado para filtrar o model `User`, retornando apenas os detalhes do usuário da requisição (`request.user`)
- `list`: utiliza o método `get_queryset()` para obter os detalhes do usuário da requisição e utiliza o serializer da view para compor a resposta da requisição

## `PerfilLogadoViewSet`

A view `PerfilLogadoViewSet` permite apenas acesso de leitura do perfil associado ao usuário da requisião (se disponível). Possui o campo:

- `serializer_class`: indica que a classe utilizada na serialização é `PerfilSerializer`

Além disso, contém os métodos:

- `get_queryset`: utilizado para filtrar o model `Perfil`, retornando apenas o perfil do usuário da requisição (`request.user`)
- `list`: utiliza o método `get_queryset()` para obter o perfil do usuário e, se existir, utiliza o `PerfilSerializer` para compor a resposta da requisição; caso contrário, o retorno é vazio e com código **404**, para indicar que o perfil não foi encontrado (usuário não possui perfil)

## `PerfilViewSet`

A view `PerfilViewSet` fornece funcionalidades para gerenciar os dados de perfis de usuários. Possui os campos:

- `queryset`: associado à lista dos perfis de usuários
- `serializer_class`: indica que a classe utilizada na serialização é `PerfilSerializer`
- `filterset_fields`: indica que é possível filtrar a lista de usuários pelos campos `usuario`, `estado_uf` e `cidade` utilizando parâmetros de URL
- `search_fields`: indica que é possível pesquisar os perfis considerando os campos `usuario.username`, `usuario.email`, `nome`, `cpf`, `telefone`, `endereco`, `estado_uf`, `cidade` e `cep` utilizando o parâmetro de URL `search`
- `permission_classes`: indica que apenas o usuário admin pode acessar a view

## `CursoViewSet`

A view `CursoViewSet` fornece funcionalidades para gerenciar os cursos da instituição. Possui os campos:

- `queryset`: associado à lista dos cursos, ordenada por nome
- `serializer_class`: indica que a classe utilizada na serialização é `CursoSerializer`

## `AlunoViewSet`

A view `AlunoViewSet` fornece funcionalidades para gerenciar os alunos da instituição. Possui os campos:

- `queryset`: associado à lista dos alunos, ordenada por nome
- `serializer_class`: indica que a classe utilizada na serialização é `AlunoSerializer`

## `MatriculaViewSet`

A view `MatriculaViewSet` fornece funcionalidades para gerenciar as matrículas de alunos nos cursos. Possui os campos:

- `serializer_class`: indica que a classe utilizada na serialização é `MatriculaSerializer`
- `filterset_fields`: indica que é possível filtrar a lista de matrículas pelos campos `curso`, `aluno`, `ano` e `semestre` utilizando parâmetros de URL

Além disso, fornece implementação do método `get_queryset` para retornar a lista de alunos conforme a seguinte regra:

- se o usuário da requisição for admin ou estiver nos grupos de usuário "Coordenação de Curso" ou "Secretaria", então retorna todas as matrículas
- caso contrário, retorna apenas as matrículas cujos usuários estejam relacionados ao usuário da requisição (por exemplo quando o aluno precisa saber quais as suas matrículas)

## `FuncionarioViewSet`

A view `FuncionarioViewSet` fornece funcionalidades para gerenciar os funcionários. Possui os campos:

- `queryset`: associado à lista dos funcionarios, ordenada por nome
- `serializer_class`: indica que a classe utilizada na serialização é `FuncionarioSerializer`

## `ProfessorViewSet`

A view `ProfessorViewSet` fornece funcionalidades para gerenciar os professores. Possui os campos:

- `queryset`: associado à lista dos professores, ordenada pelo nome do funcionário associado ao professor
- `serializer_class`: indica que a classe utilizada na serialização é `ProfessorSerializer`
- `filterset_fields`: indica que é possível filtrar a lista de professores por `curso` e `funcionario` por meio de parâmetros da URL
- `search_fields`: indica que é possível pesquisar a lista de professores considerando os campos `funcionario.nome`, `funcionario.cgu` e `curso.nome` por meio do parâmetro de URL `search`

## `OrientacaoViewSet`

A view `OrientacaoViewSet` fornece funcionalidades para gerenciar as orientações. Possui os campos:

- `serializer_class`: indica que a classe utilizada na serialização é `OrientacaoSerializer`
- `filterset_fields`: indica que é possível filtrar a lista de matrículas pelos campos `curso`, `aluno`, `professor` utilizando parâmetros de URL

Além disso, fornece implementação do método `get_queryset` para retornar a lista de orientações conforme a seguinte regra:

- se o usuário da requisição for admin ou estiver nos grupos de usuário "Coordenação de Curso" ou "Coordenação de Estágio e TCC", então retorna todas as orientações
- se o usuário é funcionário, então retorna todas as suas orientações (orientações em que ele é professor/orientador)
- caso contrário, retorna apenas as orientações cujos usuários estejam relacionados ao usuário da requisição (por exemplo quando o aluno precisa saber quais as suas orientações)

## `PropostaDeEstagioViewSet`

A view `PropostaDeEstagioViewSet` fornece funcionalidades para gerencar propostas de Estágio. Possui os campos:

- `serializer_class`: indica que a classe utilizada na serialização é `PropostaDeEstagioSerializer`
- `filterset_fields`: indica que é possível filtrar a lista de propostas de Estágio pelo campo `orientacao` utilizando parâmetros de URL

Além disso, fornece implementação do método `get_queryset` para retornar a lista de propostas de Estágio conforme a seguinte regra:

- se o usuário da requisição for admin ou estiver nos grupos de usuário "Coordenação de Curso" ou "Coordenação de Estágio e TCC", então retorna todas as propostas de Estágio
- se o usuário é está no grupo "Professor" ele é funcionário, então retorna todas as propostas nas quais ele é membro da banca
- caso contrário, retorna apenas as propostas de Estágio cujos alunos estejam relacionados ao usuário da requisição (por exemplo quando o aluno precisa saber quais as suas propostas de Estágio)

## `PropostaDeTCCViewSet`

A view `PropostaDeTCCViewSet` fornece funcionalidades para gerencar propostas de TCC. Possui os campos:

- `serializer_class`: indica que a classe utilizada na serialização é `PropostaDeTCCSerializer`
- `filterset_fields`: indica que é possível filtrar a lista de propostas de TCC pelo campo `orientacao` utilizando parâmetros de URL

Além disso, fornece implementação do método `get_queryset` para retornar a lista de propostas de TCC conforme a seguinte regra:

- se o usuário da requisição for admin ou estiver nos grupos de usuário "Coordenação de Curso" ou "Coordenação de Estágio e TCC", então retorna todas as propostas de TCC
- se o usuário é está no grupo "Professor" ele é funcionário, então retorna todas as propostas nas quais ele é membro da banca
- caso contrário, retorna apenas as propostas de TCC cujos alunos estejam relacionados ao usuário da requisição (por exemplo quando o aluno precisa saber quais as suas propostas de TCC)

## `AvaliacaoDePropostaViewSet`

A view `AvaliacaoDePropostaViewSet` fornece funcionalidades para gerenciar os avaliações de propostas. Possui os campos:

- `queryset`: associado à lista de avaliações de propostas, ordenada pelo identificador
- `serializer_class`: indica que a classe utilizada na serialização é `AvaliacaoDePropostaSerializer`
- `filterset_fields`: indica que é possível filtrar a lista de professores por `proposta`, `usuario` e `aprovada` por meio de parâmetros da URL

## `ColaboradorExternoViewSet`

A view `ColaboradorExternoViewSet` fornece funcionalidades para gerenciar os colaboradores externos. Possui os campos:

- `queryset`: associado à lista de colaboradores externos, ordenada pelo nome
- `serializer_class`: indica que a classe utilizada na serialização é `ColaboradorExternoSerializer`

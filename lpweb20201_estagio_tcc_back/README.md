# Gerenciador de Estágio e TCC (backend)

---

Este software fornece as funcionalidades de backend para o software gerenciador de atividades de Estágio e TCC.

## Dependências

A arquitetura e a estrutura deste software dependem dos seguintes pacotes:

* django
* djangorestframework
* djangorestframework-jwt
* django-cors-headers
* django-filter

Essas dependências também estão indicadas, com suas versões específicas, no arquivo `requirements.txt`, que você pode utilizar para criar seu ambiente de desenvolvimento ou de produção.

## Criar o ambiente de desenvolvimento

Para criar o ambiente de desenvolvimento, crie um ambiente virtual do python e, depois, instale as dependências descritas no arquivo `requirements.txt`.

Na sequência, como este é um projeto Django, execute as migrations:

```shell
python manage.py migrate
```

## Documentação

A [documentação](docs/readme.md) do backend apresenta mais detalhes sobre seu funcionamento e estrutura.

## Definições iniciais de registros no banco de dados

É importante considerar que o código espera uma estrutura de dados padrão, que deve ser cadastrada utilizando o django admin, conforme descrevem as seções a seguir.

### Grupos, Usuários e Permissões

Devem ser cadastrados grupos de usuários com os seguintes nomes:

* Administradores
* Aluno
* Coordenação de curso
* Coordenação de Estágio e TCC
* Professor
* Secretaria

Você pode criar usuários e associá-los a estes grupos. Também pode atribuir permissões para os grupos ou para os próprios usuários.

### Curso, Funcionários, Professores e seus usuários

Cadastre pelo menos um curso. Cadastre também funcionários e associe-os aos cursos, criando professores. Os nomes das funções dos professores não impactam a autorização do usuário, apenas serve para armazenar as informações do domínio. Os professores são importantes para relacionar com as orientações, sejam para indicar quando um professor é orientador ou participante de uma banca (mais sobre isso na sequência).

Também associe um usuário para o funcionário, ou seja:

1. cadastre o usuário
2. cadastre o funcionário
3. cadastre um registro de `FuncionarioUsuario`, relacionando os dois

### Alunos, Matrículas e seus usuários

Cadastre pelo menos um aluno e uma matrícula dele no curso. O ano e o semestre da matrícula não interferem na informação do ano e semestre da proposta.

Para utilizar as funcionalidades para alunos, cadatre pelo menos um aluno e associe um usuário para ele, ou seja:

1. cadastre o usuário
2. cadastre o aluno
3. cadastre a matrícula
4. cadastre um registro de `AlunoUsuario`, relacionando os aluno e usuário

### Colaboradores externos e seus usuários

Para utilizar as funcionalidades para colaboradores externos, cadastre pelo menos um colaborador externo e associe um usuário para ele, ou seja:

1. cadastre o usuário
2. cadastre o colaborador externo
3. cadastre um registro de `ColaboradorExternoUsuario`, relacionando os dois

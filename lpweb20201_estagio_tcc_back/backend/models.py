from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.text import slugify


class Perfil(models.Model):
    """Esta classe representa as informações do perfil de um usuário, ou seja, os dados da pessoa associada
    ao usuário"""
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.OneToOneField(User, models.CASCADE)
    nome = models.CharField(max_length=128, db_index=True)
    sexo = models.CharField(max_length=1, null=True)  # F, M
    cpf = models.CharField(max_length=14, null=True, unique=True)  # 000.000.000-00
    telefone = models.CharField(max_length=15, null=True)  # (00) 00000-0000
    endereco = models.TextField(max_length=512, null=True)
    cep = models.CharField(max_length=10, null=True)  # 00.000-000
    estado_uf = models.CharField(max_length=2, null=True)  # AA
    cidade = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    """Esta classe representa as informações de um curso"""
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Sobrescrita do método `save()` para que o slug do curso seja gerado a partir do nome"""
        self.slug = slugify(self.nome)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    """Esta classe representa as informações de um aluno (uma pessoa com quem a instituição de ensino tem vínculo
    estudantil)"""
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=128, db_index=True)
    cgu = models.IntegerField(unique=True)

    def __str__(self):
        return self.nome


class AlunoUsuario(models.Model):
    """Esta classe representa a relação entre um usuário e um aluno. É a forma de indicar que um aluno
    tem um usuário"""
    aluno = models.OneToOneField(Aluno, models.CASCADE, related_name='usuario')
    usuario = models.OneToOneField(User, models.CASCADE, related_name='aluno')

    def __str__(self):
        return '{} ({})'.format(self.aluno, self.usuario)


class Matricula(models.Model):
    """Esta classe representa as informações da matrícula de um aluno, ou seja, um aluno está matriculado em
    um curso, em um ano e semestre"""

    class Meta:
        unique_together = ['curso', 'aluno', 'ano', 'semestre']

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    ano = models.PositiveIntegerField()
    semestre = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} - {} - {}-{}'.format(self.curso, self.aluno, self.ano, self.semestre)


class Funcionario(models.Model):
    """Esta classe representa as informações de um funcionário da instituição de ensino"""
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=128, db_index=True)
    cgu = models.IntegerField(unique=True)

    def __str__(self):
        return self.nome


class FuncionarioUsuario(models.Model):
    """Esta classe representa a relação entre um funcionário e um usuário. É a forma de indicar que um
    funcionário tem um usuário"""
    funcionario = models.OneToOneField(Funcionario, models.CASCADE, related_name='usuario')
    usuario = models.OneToOneField(User, models.CASCADE, related_name='funcionario')

    def __str__(self):
        return '{} ({})'.format(self.funcionario, self.usuario)


class Professor(models.Model):
    """Esta classe representa informações de um professor, ou seja, quando um funcionário está relacionado
    a um curso com, pelo menos, a função de professor. Outras funções são: coordenador de curso;
    coordenador de Estágio e TCC"""

    class Meta:
        unique_together = ['curso', 'funcionario', 'funcao']

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='professores')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='cursos')

    class Funcoes(models.TextChoices):
        COORDENADOR = 'coordenador', 'Coordenador de curso'
        COORDENADOR_ESTAGIO_TCC = 'coordenador-estagio-tcc', 'Coordenador de Estágio e TCC'
        PROFESSOR = 'professor', 'Professor'

    funcao = models.CharField(max_length=64, choices=Funcoes.choices)

    def __str__(self):
        return '{} - {} ({})'.format(self.curso, self.funcionario, self.get_funcao_display())


class ColaboradorExterno(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=14, null=True, blank=True)  # 000.000.000-00
    email = models.EmailField(null=True, blank=True)
    instituicao = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.nome


class ColaboradorExternoUsuario(models.Model):
    colaborador_externo = models.OneToOneField(ColaboradorExterno, models.CASCADE, related_name='usuario')
    usuario = models.OneToOneField(User, models.CASCADE, related_name='membro_externo')

    def __str__(self):
        return '{} ({})'.format(self.colaborador_externo, self.usuario)


class Orientacao(models.Model):
    """Esta classe representa informações de uma orientação. Uma orientação representa um processo acadêmico
    no qual um aluno (orientando) realiza uma monografia sob a condução do professor (orientador). O tipo
    da orientação pode ser: de Estágio ou de TCC"""

    class Meta:
        unique_together = ['curso', 'aluno', 'professor', 'tipo', 'ano', 'semestre']

    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='orientacoes')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='orientacoes')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='orientacoes')

    class Tipos(models.TextChoices):
        ESTAGIO = 'estagio', 'Estágio'
        TCC = 'tcc', 'Trabalho de Conclusão de Curso (TCC)'

    tipo = models.CharField(max_length=8, choices=Tipos.choices, default=Tipos.ESTAGIO)
    ano = models.PositiveIntegerField()
    semestre = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} - {} - {}-{} ({})'.format(self.aluno, self.professor, self.ano, self.semestre,
                                             self.get_tipo_display())


class Proposta(models.Model):
    """Esta classe representa as informações de uma proposta. Uma proposta (de Estágio ou de TCC, com
    models específicos para cada situação) representa uma intenção de um aluno em realizar uma monografia. Desta
    forma, a proposta faz parte da orientação e contém elementos de projeto da monografia que são avaliados
    pelos membros da banca da orientação. A proposta é aprovada por um coordenador de Estágio e TCC"""
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    orientacao = models.OneToOneField(Orientacao, models.CASCADE)
    titulo = models.TextField(max_length=512)
    conceitos = models.TextField(max_length=4000)
    resultados_esperados = models.TextField(max_length=4000)
    aprovada = models.NullBooleanField()
    aprovada_em = models.DateTimeField(null=True, blank=True)
    aprovada_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo


class PropostaDeEstagio(Proposta):
    """Esta classe representa uma proposta de Estágio, uma especialização da proposta"""
    pass


class PropostaDeTCC(Proposta):
    """Esta classe representa uma proposta de TCC, uma especialização da proposta"""
    objetivo = models.TextField(max_length=4000)
    tecnologias = models.TextField(max_length=4000)
    metodologia = models.TextField(max_length=4000)


class MembroDeBancaDeProposta(models.Model):
    """Esta classe representa informação de um membro de banca. O membro da banca pode ser interno, ou seja,
    um funcionário (não necessariamente um professor) ou externo. Neste último caso, são armazenadas
    informações de identificação do membro de banca externo."""
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    proposta = models.ForeignKey(Proposta, models.CASCADE, related_name='membros_da_banca')
    membro_interno = models.ForeignKey(Funcionario, models.CASCADE, related_name='participacoes_em_bancas', null=True,
                                       blank=True)
    membro_externo = models.ForeignKey(ColaboradorExterno, models.CASCADE, related_name='participacoes_em_bancas',
                                       null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.membro_interno if self.membro_interno else self.membro_externo)


class AvaliacaoDeProposta(models.Model):
    """Esta classe representa informações de uma avaliação de proposta. A avaliação é realizada por um membro
    da banca (o relacionamento aqui é com usuário)"""
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='avaliacoes', null=True)
    comentario = models.TextField(max_length=5000)
    aprovada = models.NullBooleanField()
    publicada = models.NullBooleanField()

    @property
    def usuario_eh_funcionario(self):
        funcionario = FuncionarioUsuario.objects.filter(usuario=self.usuario)
        return funcionario.exists()

    @property
    def avaliador(self):
        """Retorna o avaliador da proposta de acordo com a informação associada ao usuário:

        * se o usuário do avaliador estiver relacionado a um funcionário, o avaliador é um membro interno, então retorna o funcionário
        * se o usuário do avaliador estiver relacionado a um colaborador externo, o avaliador é um membro externo, então retorna o colaborador externo
        """
        # busca o funcionário da avaliação
        r = FuncionarioUsuario.objects.filter(usuario=self.usuario)
        # se tem funcionário
        if r.exists():
            # retorna o funcionario (é um membro interno)
            return r.first().funcionario
        else:
            # o avaliador é um colaborador externo
            # busca e retorna o colaborador externo
            r = ColaboradorExternoUsuario.objects.filter(usuario=self.usuario)
            if r.exists():
                return r.first().colaborador_externo
            else:
                return None

    def __str__(self):
        return '{} - {}'.format(self.proposta, self.usuario)

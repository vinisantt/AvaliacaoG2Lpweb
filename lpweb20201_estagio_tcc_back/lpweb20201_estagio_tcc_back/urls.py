"""lpweb20201_estagio_tcc_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register('perfil-logado', views.PerfilLogadoViewSet, basename='perfil-logado')
router.register('usuario-logado', views.UsuarioLogadoDetailsViewSet, basename='usuario-logado')
router.register('perfis', views.PerfilViewSet, basename='perfis')
router.register('cursos', views.CursoViewSet)
router.register('alunos', views.AlunoViewSet)
router.register('matriculas', views.MatriculaViewSet, basename='matriculas')
router.register('funcionarios', views.FuncionarioViewSet)
router.register('professores', views.ProfessorViewSet)
router.register('orientacoes', views.OrientacaoViewSet, basename='orientacoes')
router.register('propostas-de-estagio', views.PropostaDeEstagioViewSet, basename='propostas-de-estagio')
router.register('propostas-de-tcc', views.PropostaDeTCCViewSet, basename='propostas-de-tcc')
router.register('avaliacoes-de-propostas', views.AvaliacaoDePropostaViewSet, basename='avaliacoes-de-propostas')
router.register('colaboradores-externos', views.ColaboradorExternoViewSet, basename='colaboradores-externos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/token-auth/', obtain_jwt_token),
    path(r'api/token-refresh/', refresh_jwt_token),
]

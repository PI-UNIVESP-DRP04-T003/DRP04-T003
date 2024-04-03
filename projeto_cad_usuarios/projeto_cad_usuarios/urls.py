
#Parte Login

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from projeto_cad_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pagina1/', views.pagina1, name='pagina1'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('accounts/', include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()


#Parte Cadastro
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
   #rota, view responsável, nome de referência
   #usuarios.com/usuarios
    path('',views.home,name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]

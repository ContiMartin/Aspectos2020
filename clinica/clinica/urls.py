from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mostrar_login, name='mostrar_login'),
    path('index/', views.index, name='index'),
    path('administracion/', include('administracion.urls')),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='logout'),
    path('crear_cuenta_medico', views.CrearCuentaMedico.as_view(), name='crear_cuenta_medico'),
    path('crear_cuenta_paciente', views.CrearCuentaPaciente.as_view(), name='crear_cuenta_paciente'),
    path('elegir_tipo_de_cuenta', views.elegir_tipo_de_cuenta, name='elegir_tipo_de_cuenta')
]

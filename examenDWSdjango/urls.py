from django.urls import path
from .import views

urlpatterns = [
 path('index/', views.index, name='index'),
 path('votos/ultimo_voto/', views.ultimo_voto, name='ultimo_voto'),
 path('votos/votos_menor3/<int:cliente_id>/', views.motos_votos_menor3, name='votos_menor3'),
 #path('votos/no_votan/', views.clientes_no_votan, name='no_votan'),
 path('cuentas_bancarias/<str:nombre>/', views.cuentas_bancarias_filtro_nombre, name='cuentas_nombre'),
 path('votos/votos_2023_5pts/', views.votos_cliente_2023, name='votos_2023_5pts')
]
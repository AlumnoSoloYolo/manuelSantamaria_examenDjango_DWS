from django.shortcuts import render
from django.db.models import Q,F,Prefetch, Avg
from .models import Moto, Cliente, Voto_cliente, Cuenta_bancaria

# Create your views here.


def index(request):
    return render(request, 'index/index.html')


# 1 El último voto que se realizó en un modelo principal en concreto, y mostrar el comentario, 
# la votación e información del usuario o cliente que lo realizó: 1.5 puntos
def ultimo_voto(request):
    
    voto = Voto_cliente.objects.select_related('moto', 'cliente').order_by('-fecha_voto')[0:1].get()
    return render(request, 'votos/ultimo_voto.html', {'voto': voto})


# 2 Todos los modelos principales que tengan votos con una puntuación numérica menor 
# a 3 y que realizó un usuario o cliente en concreto: 1.5 puntos
def motos_votos_menor3(request, cliente_id):
    votos = Voto_cliente.objects.filter(id=cliente_id, puntuacion__lt=3)
    motos = Moto.objects.filter(voto_moto__in=votos)

    return render(request, 'votos/motos_votos_menor3.html', {'motos': motos})




# 3 Todos los usuarios o clientes que no han votado nunca y mostrar información sobre estos usuarios y 
# clientes al completo: 1.5 puntos
#def clientes_no_votan(request):
    
 #   return render(request, 'votos/no_votan.html', {'voto': votos})


# 4 Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el 
# propietario tenga un nombre que contenga un texto en concreto, por ejemplo 
# “Juan”: 1.5 puntos
def cuentas_bancarias_filtro_nombre(request, nombre):
    cuentas = Cuenta_bancaria.objects.filter(Q(banco='CA') | Q(banco='UN')).select_related('cliente').filter(cliente__nombre__icontains=nombre)
    
    return render(request, 'cuentas_bancarias/cuentas_filtro_nombre.html', {'cuentas': cuentas})

# 5 Obtener los votos de los usuarios que hayan votado a partir del 2023 con una puntuación 
# numérica igual a 5  y que tengan asociada una cuenta bancaria. 1.5 puntos
def votos_cliente_2023(request):
    votos = Voto_cliente.objects.filter(fecha_voto__year__gte=2023, puntuacion=5).select_related('cliente')
    return render(request, 'votos/votos_2023.html', {'votos': votos})

# 6 Obtener todos los modelos principales que tengan una media de votaciones mayor del 2,5: 1.5 punto

def motos_media_alta(request):
    
    motos = Moto.objects.annotate(media_votacion=Avg('voto_moto__puntuacion')).filter(media_votacion__gt=2.5)

    return render(request, 'votos/motos_media.html', {'motos': motos})




#Páginas de Error
def mi_error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)
    




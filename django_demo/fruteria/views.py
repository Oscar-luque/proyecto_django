from django.shortcuts import render
from .models import Fruta, Cliente, Pedido
from .forms import PedidoForm
from .forms import CrearFrutaForm
from .forms import CrearClienteForm
from .forms import CrearPedidoForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
def lista_frutas(request):
    frutas = Fruta.objects.all()
    return render(request, 'fruteria/frutas.html', {'frutas': frutas})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'fruteria/clientes.html', {'clientes': clientes})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'fruteria/pedidos.html', {'pedidos': pedidos})

def editar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        form.save()
        return redirect('fruteria:lista_pedidos')
    return render(request, 'fruteria/editar_pedido.html', {'form': form, 'pedido': pedido})

def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('fruteria:lista_pedidos')
    return render(request, 'fruteria/eliminar_pedido.html', {'pedido': pedido})

def crear_fruta(request):
    form = CrearFrutaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fruteria:lista_frutas')
    return render(request, 'fruteria/crear_fruta.html', {'form': form})

def crear_cliente(request):
    form = CrearClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fruteria:lista_clientes')
    return render(request, 'fruteria/crear_cliente.html', {'form': form})

def crear_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fruteria:lista_pedidos')
    return render(request, 'fruteria/crear_pedido.html', {'form': form})
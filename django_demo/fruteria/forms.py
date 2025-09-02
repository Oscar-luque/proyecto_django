from django import forms
from .models import Pedido, Fruta, Cliente

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'frutas']

class CrearFrutaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    origen = forms.CharField(max_length=100)
    sabor = forms.CharField(max_length=50)
    precio = forms.DecimalField(max_digits=5, decimal_places=2)

    def save(self):
        nueva_fruta = Fruta(
            nombre=self.cleaned_data['nombre'],
            origen=self.cleaned_data['origen'],
            sabor=self.cleaned_data['sabor'],
            precio=self.cleaned_data['precio']
        )
        nueva_fruta.save()
        return nueva_fruta
    
class CrearClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)

    def save(self):
        nuevo_cliente = Cliente(
            nombre=self.cleaned_data['nombre'],
            email=self.cleaned_data['email'],
            telefono=self.cleaned_data['telefono']
        )
        nuevo_cliente.save()
        return nuevo_cliente
    
class CrearPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'frutas']
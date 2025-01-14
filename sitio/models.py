from django.db import models
from django.contrib.auth.models import User
from django import forms
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

# Model for product categories
class Categoria(models.Model):
    descripcion = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return f"Id: {self.pk} | Descripcion: {self.descripcion}"

# Model for employee profiles
class PerfilEmpleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='imagenes/productos/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Model for products
class Producto(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    imagen = models.FileField(upload_to='imagenes/productos/')
    descripcion = models.CharField(max_length=200, null=False)
    precio = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")

    def __str__(self) -> str:
        return f"Id: {self.pk} | Titulo: {self.titulo} | Imagen: {self.imagen} | Descripcion: {self.descripcion} | Precio: {self.precio} || Categoria_id: {self.categoria.id} "

# Model for user shopping cart
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carrito")
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self) -> str:
        return f"Id: {self.pk} | Usuario_id: {self.usuario.id} | Usuario: {self.usuario.username} | Total: {self.total}"

# Model for items in the shopping cart
class Carrito_item(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")

    def __str__(self) -> str:
        return f"Id: {self.pk} | Producto: {self.producto.titulo} | Carrito_id: {self.carrito.id}"

# Model for employee information
class empleados(models.Model):
    Nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    sueldo = models.IntegerField()

    def __str__(self):
        return f"Id: {self.pk} | Nombre: {self.Nombre} | Puesto: {self.puesto} | Sueldo: {self.sueldo}"

# Model for loan information
class prestamos(models.Model):
    nombre = models.CharField(max_length=100, default='Nombre predeterminado')
    Monto = models.IntegerField()
    TipoPago = models.CharField(max_length=90)
    FechaLimite = models.DateField()

    def __str__(self):
        return f"Id: {self.pk} | Monto: {self.Monto} | TipoPago: {self.TipoPago} | FechaLimite: {self.FechaLimite}"

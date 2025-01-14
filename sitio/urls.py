from django.urls import path,include
from . import views

app_name = "SITIO"
urlpatterns = [
    # REGISTRAR USUARIO
       
       path('registrarse/', views.register, name="register"),


    # ACERCA DE
    path('acercaDe', views.acerca_de, name="acerca_de"),
    
    # PRODUCTOS
    path('', views.producto_index, name="producto_index"),
    path('producto/agregar', views.producto_create, name="producto_create" ),
    path('producto/<int:producto_id>', views.producto_show, name="producto_show" ),
    path('producto/<int:producto_id>/editar', views.producto_edit, name="producto_edit" ),
    path('producto/<int:producto_id>/eliminar', views.producto_delete, name="producto_delete" ),
    path('producto/buscador', views.producto_search, name="producto_search"),
    path('categoria/<int:categoria_id>/productos', views.productos_por_categoria, name="productos_por_categoria"),

    # CARRITO
    path('carrito', views.carrito_index, name="carrito_index"),
    path('carrito/agregar', views.carrito_save, name="carrito_save"),
    path('carrito/clean', views.carrito_clean, name="carrito_clean"),
    path('item_carrito/<int:item_carrito_id>/eliminar', views.item_carrito_delete, name="item_carrito_delete"),
    
    
    
    #NOMINA
    path('nomina/', views.nominas, name="nomina"),
    path('transferenciaNomina/', views.SolicitarNomina,name="transferenciaNomina"),

    #prestamo
    path('Prestamos/', views.Aceptarprestamo,name='Aceptar'),
    path('SolicitarPrestamo/', views.SolicitarPrestamo,name='Solicitar'),
    path('transferenciaPrestamo/', views.transferenciaPrestamo,name="transferenciaPrestamo"),
    path('prestamoSolicitado/', views.Prestamosolicitado,name="Prestamosolicitado"),
    
    #carrito
    path('Pago/<int:product_id>/', views.proceso_pago, name="Pago"),
     

    
    #perfil
    
    path('Perfil/', views.perfil, name="perfil"),
    path('Perfilempleado/', views.perfilempleado, name="perfilempleado"),
    path('Perfiladmin/', views.perfiladmin, name="perfiladmin"),
    
    
    
    
    
    

]
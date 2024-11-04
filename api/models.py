from django.db import models

# Create your models here.

class Generos(models.Model):
    generos_id = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'generos'

class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    correo_usuario = models.CharField(max_length=255, default="example@example.com")
    password_usuario = models.CharField(max_length=20, default="default_password")
    localidad = models.CharField(max_length=255)
    fk_generos = models.ForeignKey(Generos, on_delete=models.CASCADE, default=0)
    class Meta:
        db_table = "usuarios"

class Administracion(models.Model):
    administracion_id = models.AutoField(primary_key=True)
    usuario_administracion = models.CharField(max_length=30)
    correo_administracion = models.CharField(max_length=255, default="example@example.com")
    password_administracion = models.CharField(max_length=20, default="default_password")
    class Meta:
        db_table = "administracion"

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=25)
    class Meta:
        db_table = "categoria"
        
class Estatus(models.Model):
    estatus_id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)
    class Meta:
        db_table = "estatus"

class Precio(models.Model):
    precio_id = models.AutoField(primary_key=True)
    precio = models.FloatField(max_length=7)
    class Meta:
        db_table = "precio"

class Preguntas(models.Model):
    pregunta_id =models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=150)
    respuesta = models.CharField(max_length=150)
    fk_usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE, default=0)
    class Meta:
        db_table = "preguntas"


class Mueble(models.Model):
    mueble_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    medidas =  models.CharField(max_length=30)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=0)
    fk_precio = models.ForeignKey(Precio, on_delete=models.CASCADE, default=0)
    fk_pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE, default=0)
    class Meta:
        db_table = "mueble"

class Pedidos(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    nombre_comprador = models.CharField(max_length=255)
    telefono = models.BigIntegerField(default=0)
    detalles = models.CharField(max_length=255)
    fk_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, default=0)
    fk_mueble = models.ForeignKey(Mueble, on_delete=models.CASCADE, default=0)
    fk_precio = models.ForeignKey(Precio, on_delete=models.CASCADE, default=0)
    fk_estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, default=0)
    class Meta:
        db_table = "pedidos"
from django.db import models

class Productos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_stock = models.IntegerField()
    fecha_creacion = models.DateField()
    fecha_ultima_modificacion = models.DateField()

    class Meta:
        managed = True
        db_table = 'productos'


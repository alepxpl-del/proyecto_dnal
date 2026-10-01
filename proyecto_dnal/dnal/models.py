from django.db import models

class Maquina(models.Model):
    TIPOS = [
        ("Motosierra", "Motosierra"),
        ("Desmalezadora", "Desmalezadora"),
        ("Cortadora de césped", "Cortadora de césped"),
        ("Generador", "Generador"),
        ("Bomba de agua", "Bomba de agua"),
        ("Taladro", "Taladro"),
        ("Percutor", "Percutor"),
        ("Pulidora", "Pulidora"),
        ("Amoladora", "Amoladora"),
        ("Compresor", "Compresor"),
        ("Otra", "Otra"),
    ]
    MARCAS = [
        ("Lusqtoff", "Lusqtoff"),
        ("Daewoo", "Daewoo"),
        ("Einhell", "Einhell"),
        ("Otra", "Otra"),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    marca = models.CharField(max_length=50, choices=MARCAS)
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.marca} {self.modelo}"

class Reparacion(models.Model):
    ESTADOS = [
        ("Ingresada", "Ingresada"),
        ("En reparación", "En reparación"),
        ("Lista para retirar", "Lista para retirar"),
        ("Entregada", "Entregada"),
    ]
    maquina = models.ForeignKey(Maquina,on_delete=models.CASCADE)
    problema = models.TextField()
    trabajo_realizado = models.TextField(blank=True)
    repuestos = models.TextField(
        blank=True,
        help_text="Indicar los repuestos utilizados."
    )
    costo_repuestos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    costo_mano_obra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    estado = models.CharField(
        max_length=50,
        choices=ESTADOS,
        default="Ingresada"
    )
    fecha_ingreso = models.DateField(auto_now_add=True)

    fecha_entrega = models.DateField(
        null=True,
        blank=True
    )
    @property
    def costo_total(self):
        return self.costo_repuestos + self.costo_mano_obra
    
    def __str__(self):
        return f"Reparación de {self.maquina}"
    
    class Meta:
            verbose_name = "Reparación"
            verbose_name_plural = "Reparaciones"
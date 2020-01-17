from django.db import models

# Create your models here.

class Empresa(models.Model):
    
    ramos_de_atividade = (
        ('P','publica'),
        ('PV','privado'),
        ('ONG','sem fins lucrativos')

    )
    portes_tamanho = (
        ('P','pequena'),
        ('M','media'),
        ('G','grande')
    )

        

    nome = models.CharField(max_length=255,)
    endereço = models.CharField(max_length=255, )
    cnpj = models.IntegerField()
    telefone = models.IntegerField()
    ramo_de_atividade = models.CharField(max_length=255, choices=ramos_de_atividade)
    porte_tamanho = models.CharField(max_length=255, choices=portes_tamanho )


    def __str__(self):
        return self.nome

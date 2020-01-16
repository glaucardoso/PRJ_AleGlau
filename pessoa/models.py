from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    telefone = models.IntegerField(verbose_name='Telefone')
    email = models.CharField(max_length=50, verbose_name='E-mail')
    generos = (
        ("M", "Feminino"),
        ("F", "Feminino")
    )
    genero = models.CharField(verbose_name='Gênero', choices=generos)
    cargos = (
        ("Aprendiz"),
        ("Assistente"),
        ("Técnico"),
        ("Analista"),
        ("Supervisor"),
        ("Gerente"),
        ("Diretor"),
    )
    cargo = models.CharField(verbose_name='Cargo', choices=cargos)
    pretencao_salarial = models.FloatField(verbose_name="Pretenção Salarial")
    pcd = models.BooleanField(verbose_name="Possui alguma Deficiência?")
    objetivo = models.TextField(verbose_name="Objetivo Pretendido")



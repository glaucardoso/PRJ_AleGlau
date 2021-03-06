from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    telefone = models.IntegerField(verbose_name='Telefone')
    email = models.CharField(max_length=50, verbose_name='E-mail')
    generos = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )
    genero = models.CharField(max_length=255, verbose_name='Gênero', choices=generos)
    cargos = (
        ("APRENDIZ", "Aprendiz"),
        ("ASSISTENTE", "Assistente"),
        ("TÈCNICO", "Técnico"),
        ("ANALISTA", "Analista"),
        ("Supervisor", "Supervisor"),
        ("GERENTE", "Gerente"),
        ("DIRETOR", "Diretor"),
    )
    cargo = models.CharField(max_length=255, verbose_name='Cargo', choices=cargos)
    pretencao_salarial = models.FloatField(verbose_name="Pretenção Salarial")
    pcd = models.BooleanField(verbose_name="Possui alguma Deficiência?")
    objetivo = models.TextField(verbose_name="Objetivo Pretendido")



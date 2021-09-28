from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estado(models.Model):
    nome = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return self.nome

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return self.nome + ", " + self.estado.nome

class Local(models.Model):
    nome = models.CharField(max_length=100, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=4)
    complemento = models.CharField(max_length=10, blank=True, null=True)
    cep = models.CharField(max_length=8)
    referencia = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome + ", " + self.cidade.nome

class Pessoa(models.Model):
    class Meta:
        abstract = True

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    SEXO_CHOICE = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhum")
    )
    idade = models.IntegerField()
    altura = models.FloatField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICE, default="N")

    def __str__(self) -> str:
        try:
            return self.usuario.username
        except AttributeError:
            return super().__str__()


class TipoPrioridade(models.Model):
    razao_prioridade = models.CharField(max_length=100, null=True)
    descricao_prioridade = models.CharField(max_length=100, blank=True, null=True)
    idade_minima = models.IntegerField(blank=True, null=True)
    idade_maxima = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.razao_prioridade

class Vacina(models.Model):
    nome = models.CharField(max_length=50, null=True)
    fabricante = models.CharField(max_length=50, null=True)
    pais_de_origem = models.CharField(max_length=50, null=True)
    tempo_para_segunda_dose = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.nome

class PontoVacinacao(models.Model):
    endereco = models.ForeignKey(Local, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.vacina.nome + ": " + self.endereco.nome

class Vacinacao(models.Model):
    ponto_vacinacao = models.ForeignKey(PontoVacinacao, on_delete=models.CASCADE, null=True)
    data = models.DateTimeField(null=True)
    
    def __str__(self) -> str:
        return f"{self.ponto_vacinacao}" + "-> " + f"{self.data}"

class Paciente(Pessoa):
    prioridade = models.ForeignKey(
        TipoPrioridade,
        on_delete=models.CASCADE
    )
    vacinacao = models.ForeignKey(Vacinacao, on_delete=models.CASCADE, null=True)
    ja_tomou_primeira_dose = models.BooleanField(default=False)

class Enfermeiro(Pessoa):
    pass

class Gestor(Pessoa):
    pass

class Administrador(Pessoa):
    pass

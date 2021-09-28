from django.contrib import admin
from .models import Paciente, Enfermeiro, Gestor, Administrador, TipoPrioridade, Estado, Cidade, Local, Vacina, Vacinacao, PontoVacinacao


# Register your models here.

admin.site.register(Paciente)
admin.site.register(Enfermeiro)
admin.site.register(Gestor)
admin.site.register(Administrador)
admin.site.register(TipoPrioridade)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Local)
admin.site.register(Vacina)
admin.site.register(Vacinacao)
admin.site.register(PontoVacinacao)


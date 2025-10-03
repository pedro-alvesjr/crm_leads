from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Perfil(models.Model):
    ROLE_CHOICES = (
        ('DONO', 'Dono'),
        ('GESTOR', 'Gestor'),
        ('PARCEIRO', 'Parceiro'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    gestor = models.ForeignKey(
        'self',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='parceiros'
    )

    def __str__(self):
        return f"{self.user.username} ({self.role})"
    
class Lead(models.Model):
    STATUS_CHOICES = (
        ('ATIVA_INFO', 'Ativa com informações'),
        ('ATIVA_DOCS', 'Ativa com documentos em falta'),
        ('ATIVA_ANALISE', 'Ativa com processo em análise'),
        ('APROVADA', 'Ativa com projeto aprovado'),
        ('DESATIVADA', 'Lead desativada'),
    )

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ATIVA_INFO')

    parceiro = models.ForeignKey(
        Perfil,
        limit_choices_to={'role': 'PARCEIRO'},
        on_delete=models.CASCADE,
        related_name='leads'
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.get_status_display()}"
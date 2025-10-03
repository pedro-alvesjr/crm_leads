# CRM Leads

Projeto Django simples para gestão de leads, com três níveis de permissão:  
- **Dono**: vê todas as leads  
- **Gestor**: vê apenas leads dos seus parceiros  
- **Parceiro**: vê apenas as suas próprias leads  

Inclui dashboard com contagem de leads por status, listagem e criação de leads.

## Estrutura

```
crm_leads/
├── crm_leads/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── dashboard.html
│       ├── lista_leads.html
│       └── criar_lead.html
└── manage.py
```

## Instalação

1. Criar ambiente virtual:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
2. Instalar dependências:
```
pip install django
```
3. Criar migrações e migrar:
```
python manage.py makemigrations
python manage.py migrate
```
4. Rodar servidor:
```
python manage.py runserver
```

## Perguntas do Projeto

**Q1: Sistema de Permissões**  
Podemos usar filtros no Django ORM com base na relação entre usuários e leads.
- Dono: `Lead.objects.all()`  
- Gestor: `Lead.objects.filter(parceiro__gestor=request.user)`  
- Parceiro: `Lead.objects.filter(parceiro=request.user)`  

**Q2: Preparação SaaS**  
Adicionar campo `empresa` ao model Lead para suportar multi-tenant:
```python
empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
```
Query SaaS-ready:
```python
Lead.objects.filter(empresa=request.user.empresa)
```

**Q3: Otimização Performance**  
Com 10.000+ leads, usar agregação:
```python
from django.db.models import Count
Lead.objects.values('status').annotate(count=Count('status')).order_by('status')
```

## Autor
Pedro Alves
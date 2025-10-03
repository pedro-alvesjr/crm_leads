from django.shortcuts import render, redirect
from django.db import models
from .models import Lead
from django import forms

# Dashboard
def dashboard(request):
    contagem = Lead.objects.values('status').order_by('status').distinct().annotate(count=models.Count('status'))
    return render(request, 'dashboard.html', {'contagem': {c['status']: c['count'] for c in contagem}})

# Lista de leads
def lista_leads(request):
    leads = Lead.objects.all()
    return render(request, 'lista_leads.html', {'leads': leads})

# Formulário para criar Lead
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['nome', 'email', 'telefone', 'status', 'parceiro']

# Criar nova lead
def criar_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_leads')  # Melhor prática
    else:
        form = LeadForm()
    return render(request, 'criar_lead.html', {'form': form})
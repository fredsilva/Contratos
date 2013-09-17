# encoding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from datetime import date
from models import Contrato
from forms import ContratoForm, CargoForm

ANO_ATUAL = date.today().year

def home(request):	
	context = {'titulo': 'Sistema de Gestão de Contratos - Sefaz/TO', 'pagina': 'Home', 'breadcrumb': []}
	return render(request, 'home.html', context)

def cargos(request):
	context = {'pagina': 'Cargos', 'breadcrumb': ['Cargos']}
	return render(request, 'cargos.html', context)


def contratos(request):	
	contratos = Contrato.objects.all()
	context = {'pagina': 'Contratos', 'breadcrumb': ['Contratos']}	
	context['contratos'] = contratos
	return render(request, 'contratos.html', context)	


def rodape(request):
	context = {'ano_atual': ANO_ATUAL}
	return render(request, 'rodape.html',context)

''' Views de cadastros '''
# ==============================================================================
def addContrato(request):	
	context = {'pagina': 'Novo Contrato', 'breadcrumb': ['Novo-Contrato']}	
	if request.method == 'POST':
		form['form'] = form = ContratoForm(request.POST)
		if form.is_valid():
			contrato = form.save()
	else:
		context['form'] = form = ContratoForm()
	return render(request, 'addContrato.html', context)

def addCargo(request):
	context = {'pagina': 'Novo Cargo', 'breadcrumb': ['Novo-Cargo']}
	if request.method == 'POST':
		context['form'] = form = CargoForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			context = {'mensagem': 'Cargo cadastrado com sucesso!', 'breadcrumb': ['Confirmação']}
			return render(request,'confirma.html', context)
			#return redirect('/confirma/')
	else:	
		context['form'] = form = CargoForm()

	return render(request, 'addCargo.html', context)

# ==============================================================================

''' Generic Views '''
# ==============================================================================
class ContratosList(generic.ListView):
	template_name = 'contratos.html'

	def get_queryset(self):
		return Contrato.objects.all()

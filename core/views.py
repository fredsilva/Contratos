# encoding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from datetime import date
from models import Contrato, Cargo
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
	''' Cadastra novo contrato '''

	context = {'pagina': 'Novo Contrato', 'breadcrumb': ['Novo-Contrato']}	
	if request.method == 'POST':
		context['form'] = form = ContratoForm(request.POST)
		if form.is_valid():
			context['mensagem'] = 'Contrato cadastrado com sucesso!'			
			contrato = form.save()
			return render(request, 'confirma.html', context)
	else:
		context['form'] = form = ContratoForm()
	return render(request, 'addContrato.html', context)

def addCargo(request):
	''' Cadastra novo cargo '''

	context = {'pagina': 'Novo Cargo', 'breadcrumb': ['Novo-Cargo']}
	if request.method == 'POST':
		context['form'] = form = CargoForm(request.POST)
		if form.is_valid():
			cargo = form.save()
			context['mensagem'] = 'Cargo cadastrado com sucesso!'
			return render(request,'confirma.html', context)
			#return redirect('/confirma/')
	else:	
		context['form'] = form = CargoForm()

	return render(request, 'addCargo.html', context)

# ==============================================================================

''' Generic Views '''
# ==============================================================================
class CargoList(generic.ListView):
	''' View para listar todos os cargos cadastrados '''

	template_name = 'cargos.html'	
	context_object_name = 'cargos'
	paginate_by = 2

	def get_queryset(self):		
		return Cargo.objects.all()

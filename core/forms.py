# encoding: utf-8
from django.forms import ModelForm
from models import Contrato, Cargo

class ContratoForm(ModelForm):

	class Meta:
		model = Contrato
		exclude = ['situacao', 'numero', 'ano']

class CargoForm(ModelForm):

	class Meta:
		model = Cargo
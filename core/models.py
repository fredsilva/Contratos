# encoding: utf-8
from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length = 50, unique = True, blank = False)

    def __unicode__(self):
        return self.nome

class Gestor(models.Model):
    nome  = models.CharField(max_length = 80)
    cargo = models.ForeignKey("Cargo", verbose_name = 'Cargo')

class TipoContrato(models.Model):
    decricao = models.CharField(max_length = 50)

class Origem(models.Model):
    descricao = models.CharField(max_length = 50)

class UnidadeGestora(models.Model):
    nome   = models.CharField(max_length = 50)

class UnidadeSolicitante(models.Model):
    nome   = models.CharField(max_length = 50)
    gestor = models.ForeignKey("Gestor")

class Interessado(models.Model):
    cpfCnpj     = models.CharField(max_length = 14)
    razaoSocial = models.CharField(max_length = 80)

class Notificacoes(models.Model):
    descricao    = models.TextField()
    ativa        = models.BooleanField()
    dataAtivacao = models.DateField()
    contrato     = models.ForeignKey("Contrato")

class TermoAditivo(models.Model):
    descricao = models.CharField(max_length = 50)
    valor     = models.DecimalField(max_digits=15, decimal_places=2)
    inicio    = models.DateField()
    fim       = models.DateField()
    contrato  = models.ForeignKey("Contrato")

class UnidadeGestorasContrato(models.Model):
    contrato       = models.ForeignKey("Contrato")
    unidadeGestora = models.ForeignKey("UnidadeGestora")
    valor          = models.DecimalField(max_digits=15, decimal_places=2)

class InteressadosContrato(models.Model):
    contrato    = models.ForeignKey("Contrato")
    interessado = models.ForeignKey("Interessado")
    percentual  = models.DecimalField(max_digits=3, decimal_places=2)

class Fiscal(models.Model):
    nome = models.CharField(max_length = 80)
    matricula = models.IntegerField()
    cargo     = models.ForeignKey("Cargo")

class FiscalSuplente(models.Model):
    nome = models.CharField(max_length = 80)
    matricula = models.IntegerField()
    cargo     = models.ForeignKey("Cargo")

class Contrato(models.Model):

    MODALIDADE_LICITACAO = (
        ('Concorrência', 'Concorrência'),
        ('Convite', 'Convite'),
        ('Pregão', 'Pregão'),
    )

    TIPO_PAGAMENTO = (
    	('Mensal', 'Mensal'),
    	('Semestral', 'Semestral'),
    	('Anual', 'Anual'),
    )

    numero              = models.IntegerField(verbose_name = u'Número')
    ano                 = models.IntegerField(verbose_name = u'Ano')
    processo            = models.CharField(max_length = 16, verbose_name = u'Processo')
    modalidadeLicitacao = models.CharField(max_length = 30, verbose_name = u'Modalidade Licitação', choices = MODALIDADE_LICITACAO)
    objeto              = models.TextField(verbose_name = u'Objeto do Contrato')
    dataInicial         = models.DateField(verbose_name = u'Início Vigência')
    dataFinal           = models.DateField(verbose_name = u'Fim Vigência')
    situacao            = models.CharField(max_length = 50, verbose_name = u'Sitação do Contrato')
    valorTotal          = models.DecimalField(max_digits=15, decimal_places=2, verbose_name = u'Valor Total')
    valorParcela        = models.DecimalField(max_digits=15, decimal_places=2, verbose_name = u'Valor Parcela')
    valorReajuste       = models.DecimalField(max_digits=15, decimal_places=2, verbose_name = u'Valor Reajuste')
    tipoPagamento       = models.CharField(max_length=30, verbose_name = 'Tipo de Pagamento', choices=TIPO_PAGAMENTO)
    avisoVigencia       = models.IntegerField(verbose_name = u'Prazo gerar Notificacoes')
    unidadeSolicitante  = models.ForeignKey("UnidadeSolicitante", verbose_name = u'Unidade Solicitante')
    tipoContrato        = models.ForeignKey("TipoContrato", verbose_name = u'Tipo de Contrato')
    origem              = models.ForeignKey("Origem", verbose_name = u'Origem do Contrato')
    fiscal              = models.ForeignKey("Fiscal", verbose_name = u'Fiscal')
    FiscalSuplente      = models.ForeignKey("FiscalSuplente", verbose_name = u'Fiscal Suplente')
    #arquivo             = models.FileField(upload_to=None[, height_field=None, width_field=None, max_length=100, **options])

    def __unicode__(self):
        return self.numero+"/"+self.ano
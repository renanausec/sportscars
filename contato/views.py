from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Inquiry, Contato
#from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        carro_nome = request.POST['carro_nome']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        email = request.POST['email']
        telefone = request.POST['telefone']
        mensagem = request.POST['mensagem']
        user_id = request.POST['user_id']
        carro_url = request.POST['carro_url']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Inquiry.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "Você já enviou este pedido! Favor aguarde até um de nossos atendentes entrar em contato.")
                return redirect('../carros/'+carro_url)

        inq = Inquiry(user_id=user_id, car_id=car_id, carro_url=carro_url, carro_nome=carro_nome, nome=nome, sobrenome=sobrenome,
        customer_need=customer_need, cidade=cidade, estado=estado, email=email, telefone=telefone, mensagem=mensagem)

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email

        # send_mail(
        #     'Nova Inquiry - SportsCars',
        #     'Você recebeu uma nova Inquiry para o carro: ' + carro_nome + '. Por favor, faça seu login na area do Admin e veja mais detalhes.',
        #     'renanr.ausec@gmail.com',
        #     [admin_email],
        #     fail_silently=False
        # )

        inq.save()
        messages.success(request, 'Sua mensagem foi enviada com sucesso! Entraremos em contato assim que possível.')
        return redirect('../carros/'+carro_url)
    
import logging

# Inicialize o logger
logger = logging.getLogger(__name__)

def contato(request):
    if request.method == 'POST':
        logger.debug('Recebida uma solicitação POST para a view contato')

        try:
            user_id = request.POST['user_id']
            nome = request.POST['nome']
            email = request.POST['email']
            telefone = request.POST['telefone']
            assunto = request.POST['assunto']
            mensagem = request.POST['mensagem']
            
            logger.debug(f'Campos do formulário: nome={nome}, email={email}, telefone={telefone}, assunto={assunto}, mensagem={mensagem}')

            if request.user.is_authenticated:
                user_id = request.user.id
                logger.debug(f'Usuário autenticado com ID: {user_id}')

                has_contacted = Contato.objects.filter(user_id=user_id).exists()
                if has_contacted:
                    messages.error(request, "Você já enviou este pedido! Favor aguarde até um de nossos atendentes entrar em contato.")
                    logger.debug('Usuário já enviou um contato. Redirecionando de volta para a página de contato.')
                    return redirect('/contato')

            contato = Contato(user_id=user_id, nome=nome, email=email, telefone=telefone, assunto=assunto, mensagem=mensagem)
            contato.save()
            logger.debug('Dados de contato salvos com sucesso no banco de dados.')
            messages.success(request, 'Sua mensagem foi enviada com sucesso! Entraremos em contato assim que possível.')
            return redirect('/contato')

        except Exception as e:
            logger.error(f'Ocorreu um erro ao processar a solicitação de contato: {e}')
            messages.error(request, 'Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente mais tarde.')
            return redirect('/contato')
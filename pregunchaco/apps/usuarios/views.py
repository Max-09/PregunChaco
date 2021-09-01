from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import login

from . import forms
from .tokens import account_activation_token
from apps.usuarios.models import Usuario

# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta'
            message = render_to_string(
                'usuarios/email.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }
            )
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'usuarios/correo.html')


    else:
        form = forms.UserRegisterForm()
    
    context = {'form': form}
	
    return render(request, 'usuarios\Register.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Usuario.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Usuario.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('index')

    else:
        return HttpResponse('Link de activación inválido')
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm (request.POST)
        
        if form.is_valid():
            name= form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            dia_da_reserva = form.cleaned_data['dia_da_reserva']
            telefone = form.clean_data['telefone']
            
            html = render_to_string('contact/emails/contactform.html',{
                'name': name,
                'email': email,
                'content':content,
                'dia_da_reserva' : dia_da_reserva,
                'telefone' : telefone,
            })
            
            print('the form is valid')
            send_mail('The contact form subject', 'Congrats', 'noreply@gmail.com', ['email@gmail.com'], html_message=html) 
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact/index.html', {
        'form': form
    })
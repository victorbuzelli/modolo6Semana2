from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    telefone = forms.CharField()
    dia_da_reserva = forms.CharField(widget=forms.Textarea)
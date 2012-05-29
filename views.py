from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    message = forms.Field(widget=forms.Textarea)

def enviar(self):
	title = 'Message sent from Bicoblog'
	destiny = 'email@email.com'
	text = """
	Name: %(name)s
	E-mail: %(email)s
	Message:
	%(message)s
	""" % self.cleaned_data

	send_mail(
		subject=title,
		message=text,
		from_email=destiny,
		recipient_list=[destiny],
	)

def contact(request):
    if request.method == 'POST':
    	form = ContactForm(request.POST)

    	if form.is_valid():
    		form.send()
    		show = 'Message sent!'
    else:
    	form = ContactForm()
    return render_to_response(
        'contact.html',
        locals(),
        context_instance=RequestContext(request),
        )
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from validate_email import validate_email


# Create your views here.pip install pyDNS
def index(request):
    if 'action' in request.POST:
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            is_valid = validate_email(email, verify=True)
            context = {'email_valid': is_valid, 'email': email}
            return render(request, 'validate_emails/index.html', context)

    return render(request, 'validate_emails/index.html')


#    return HttpResponse('Hello from Validate Emails')


# Create your views here.
def validate(request):
    # if request.POST.get('action'):
    #     print("Button Clicked!")
    if 'action' in request.GET:
        print("Error")
    return render(request, 'validate_emails/validate.html', {
        'custom': 'Submit'
    })


class EmailForm(forms.Form):
    email = forms.EmailField()

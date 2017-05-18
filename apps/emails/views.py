from django.shortcuts import render,redirect, HttpResponse
from .models import Email

def index(request):
    if not 'errors' in request.session:
        request.session['errors'] = []
    return render(request, 'emails/index.html')

def email(request):
    if request.method=="POST":
        result = Email.objects.login(request.POST['email'])
        if result[0]:
            request.session['email'] = result[1].email
            request.session.pop('errors')
            return redirect('/results')
        else:
            request.session['errors'] = result[1]
            return redirect('/')
    else:
        return redirect('/')

def results(request):
    emails= Email.objects.all()
    return render(request,'emails/results.html', {'emails': emails, 'your_email': request.session.get('email')})

def delete(request,id):
    result = Email.objects.delete(id)
    if result[0]:
        return redirect('/results')
    else:
        print result[1]

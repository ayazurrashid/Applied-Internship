from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from .forms import comp_form
from .models import company_form


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = comp_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            pincode = form.cleaned_data['pincode']
            discription = form.cleaned_data['discription']
            email = form.cleaned_data['email']
            url = form.cleaned_data['url']
            password = form.cleaned_data['password']
            p =company_form(name=name,title=title,address=address,city=city,pincode=pincode,discription=discription,email=email,url=url,password=password)
            p.save()
            return HttpResponseRedirect(reverse('formapp:show'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = comp_form()

    return render(request, 'formapp/name.html', {'form': form})

def show(request):
    rows =company_form.objects.all()
    return render(request,'formapp/done.html', {'rows': rows})

def search(request):
    if request.method == 'POST':
        c = company_form.objects.get(id=1)
        arg=[c.id, c.name,c.title,c.address,c.city,c.pincode,c.discription,c.email,c.url,c.password]
        try:
            html = (arg)
            return HttpResponse(html)
        except company_form.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'formapp/done.html')
        
def edit(request,id):
    company = company_form.objects.get(id=id)
    context={'company':company}
    return render(request, 'formapp/edit.html',context)

def update(request,id):
    company = company_form.objects.get(id=id)
    company.name=request.POST['name']
    company.title=request.POST['title']
    company.address=request.POST['address']
    company.city=request.POST['city']
    company.pincode=request.POST['pincode']
    company.discription=request.POST['discription']
    company.email=request.POST['email']
    company.url=request.POST['url']
    company.password=request.POST['password']
    company.save()
    return HttpResponseRedirect(reverse('formapp:show'))
def delete(request,id):
    company = company_form.objects.get(id=id)
    company.delete()
    return HttpResponseRedirect(reverse('formapp:show'))
from django.shortcuts import render , render_to_response ,redirect , reverse,get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate , logout , login
from django.views.generic import ListView , View ,DeleteView ,CreateView ,RedirectView , DetailView
from .models import contacts
from accounts.models import User

# Create your views here.
def add_contact(request):
    username = request.session['username']
    instance = User.objects.get(username = username)
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        company_name = request.POST.get("company_name")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        contact_type = request.POST.get('contact_type')
        p = contacts(user=instance, fname = fname , lname = lname ,phone=phone, company_name =company_name, email = email, address =address, contact_type =contact_type )
        print(contact_type)
        p.save()

    context = {

    }
    return render(request,'add_contact.html',context)

def list_contact_customer(request):
    username = request.session['username']
    instance = User.objects.get(username = username)
    queryset = contacts.objects.filter(contact_type = "custumer" , user = instance)
    context = {
        "customer_list":queryset
    }
    return render(request , "listcustomers.html" , context)

def list_contact_vendor(request):
    username = request.session['username']
    instance = User.objects.get(username = username)
    queryset = contacts.objects.filter(contact_type = "vendor" , user = instance)
    context = {
        "vendor_list":queryset
    }
    return render(request , "listvendors.html" , context)

def contacts_detail(request , id = None):
    username = request.session['username']
    instance = get_object_or_404(contacts , id = id)
    context = {
        "instance":instance
    }
    return render(request , "detailcontact.html" , context)

def list_contact_customer_filter(request):
    username = request.session['username']
    instance = User.objects.get(username = username)
    queryset = contacts.objects.filter(contact_type = "custumer" , user = instance)
    context = {
        "customer_list":queryset
        }
    return render(request , "listcustomers.html" , context)

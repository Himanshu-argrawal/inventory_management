from django.shortcuts import render , render_to_response ,redirect , reverse,get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate , logout , login
from django.views.generic import ListView , View ,DeleteView ,CreateView ,RedirectView , DetailView
from .models import product
from accounts.models import User
from .forms import product_addform
def product_add(request):

    username = request.session['username']
    instance = User.objects.get(username = username)
    if request.method == "POST":
        name = request.POST.get('name')
        product_code = request.POST.get('product_code')
        product_minstock = request.POST.get('product_minstock')
        product_count = request.POST.get('product_count')
        product_cost = request.POST.get("product_cost")
        product_sell = request.POST.get('product_sell')
        tax_rate = request.POST.get("tax_rate")
        tax_name = request.POST.get("tax_name")
        product_total = request.POST.get("product_count")
        p = product(user = instance , name = name ,product_code = product_code, product_cost = product_cost,
                    product_count = product_count , product_minstock = product_minstock,product_total = product_total ,
                    tax_rate = tax_rate ,product_sell = product_sell,tax_name = tax_name  )
        p.save()
        return redirect('/products/show')
    context = {

    }
    return render(request , "addproduct.html" ,context)

def product_show(request):
    username = request.session['username']
    instance = User.objects.get(username = username)
    product_instance = product.objects.filter(user = instance)
    context = {
        "product":product_instance,
        
    }
    return render(request , "prouct_show.html" , context)
    
def product_detail(request , id = None):
    username = request.session['username']
    instance = get_object_or_404(product , id = id)
    context = {
        "instance":instance
    }
    return render(request , "product_details.html" , context)

def product_adjust(request , id = None):
    username = request.session['username']
    inst = User.objects.get(username = username)
    print(inst)
    instance = get_object_or_404(product , id = id)
    if request.method == "POST":
        product_add_quantity = int(request.POST.get('product_quantity_add')) + instance.product_count
        product_new_value = int(request.POST.get('product_new_value'))
        print(product_new_value)
        object_list = product.objects.filter(id = id ).update(product_cost = product_new_value ,
                                                              product_count = product_add_quantity)
        return redirect('/product/detail/%s'%(instance.id))


    context = {
        "instance":instance
    }
    return render(request , "product_adjust.html" ,context)

def product_show_adjust(request):
    username = request.session['username']
    instance = User.objects.get(username = username)
    product_instance = product.objects.filter(user = instance)
    context = {
        "product":product_instance,

    }
    return render(request , "listadjust.html" , context)

def invoiceprice(request):
    user = request.session['username']
    inst = User.objects.get(username = user)
    c = request.GET.get('product')
    e = "this is a tes"
    print(c)
    product_instance = product.objects.filter(user = inst , name = c)
    return HttpResponse(product_instance)
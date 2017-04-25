from django.shortcuts import render
from accounts.models import User
from django.views.generic import View
from .models import Invoice , invoice_link
from Product.models import product
import datetime
from django.shortcuts import render , render_to_response ,redirect , reverse,get_object_or_404
# Create your views here.
def invoicegenerate(request):
    user = request.session['username']
    instance =User.objects.get(username = user)
    productinstance = product.objects.filter(user=instance)
    if request.method == "POST":
        productcount = request.POST.get("productcount")
        total = request.POST.get('invoiceTotal')
        print(total)
        i = Invoice(name=instance , total=total , created_date=datetime.datetime.now())
        print(productcount)
        i.save()
        pid =i.id
        for number in range(1,int(productcount)+1):
            c = "quantity"+str(number)
            d = "price"+str(number)
            quantity = request.POST.get(c)
            price = request.POST.get(d)
            invoiceobject = Invoice.objects.get(id=pid)
            invoicelink = invoice_link(invoice_id = invoiceobject ,quantity = quantity , price= price )
            invoicelink.save()
    context ={"productinstance":productinstance}
    return render(request , "invoices.html" , context)

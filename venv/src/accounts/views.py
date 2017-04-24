from django.shortcuts import render , render_to_response ,redirect , reverse,get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate , logout , login
from django.urls import reverse , reverse_lazy
from django.views.generic import ListView , View ,DeleteView ,CreateView ,RedirectView , DetailView , TemplateView
from .models import User
from .forms import Register_form , Register_formTwo ,LoginForm

# Create your views here.
class Homepage(TemplateView):
    template_name = "index.html"

class Register(View):
    def get(self , request):
        user = request.user
        form = Register_form()
        return render(request ,'register.html',{'form':form})
    def post(self , request):
        form = Register_form(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/steptwo/%s'%(user.id))
        return render(request , 'register.html' , {"form":form})

def registertwo(request , id= None):
    instance = get_object_or_404(User , id=id)
    user = request.user
    form =Register_formTwo(request.POST or None , request.FILES or None , instance =instance)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form":form,
    }
    return render(request , "registertwo.html" , context)

class Login(View):

    def get(self, request):
        user = request.user
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if username and password:
                try:
                    user = User.objects.get(username = username)
                    if (user.username == username and user.password ==password):
                        request.session['username'] = username
                        request.session['password'] = password
                        uname = request.session['username']
                        return redirect('/accounts/dashboard/')
                    else:
                        return HttpResponseRedirect(reverse_lazy('home'))
                except:
                    pass

        return render(request, 'login.html', {'form': form})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/accounts/login/')

class Home(View):
    def get(self , request):
        try:
            print(request.user)
            uname = request.session['username']
            instance = get_object_or_404(User , username = uname)
            context = {
            "instance":instance,
            }
            return render(request , "dashboard.html" , context)
        except:
            print("page not found")
            return redirect('/accounts/login')

        return redirect(request ,"dashboard.html" , {})




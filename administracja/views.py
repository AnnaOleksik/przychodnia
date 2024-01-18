from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Lekarze,Cennik,Category,Product
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    return render(request,'administracja/product/list.html',{'category':category,'categories':categories,'products':products})
def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug)
    return render(request,'administracja/product/detail.html',{'product':product})


def dashboard(request):
    products=Product.objects.all()
    context={
        'products': products
        }
    return render(request,
                  'administracja/product/list.html',
                  context)

@login_required
def pass_change(request):
    return render(request,
                  'password_change.html',
                  {'section': 'password_change'})

@login_required
def password_change_done(request):
    return render(request,
                  'administracja/password_change_done.html',
                  {'section': 'administracja/password_change_done'})  
                   
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem.')
                    
                else:
                    return HttpResponse('Konto jest zablokowane.')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()
    return render(request, 'administracja/login.html', {'form': form})
   
   

def register(request):
    user_form=UserRegistrationForm(request.POST)
    if request.method=="POST":
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'register_done.html',{'new_user':new_user})
        else:
            user_form=UserRegistrationForm()
    return render(request,'register.html',{'user_form':user_form})

def index(request):
    lek=Lekarze.objects.all()
    context={
        'lek': lek
        }
    return render(request,"index.html",context)

def lista_lekarzy(request):
    lek=Lekarze.objects.all()
    context={
        'lek': lek
        }
    return render(request,"lista_lekarzy.html",context)
def oferta(request):
    products=Product.objects.all()
    context={
        'products': products
        }
    return render(request,"'administracja/product/list.html'",context)
@login_required
def cenniki(request):
    ceny=Cennik.objects.filter()
    context={
        'ceny': ceny
        }
    return render(request,{'ceny':ceny})

def cennik_pojedynczy(request):
    cena=get_object_or_404(Cennik,name=name)
    
    return render(request,'cennik.html',{'cena':cena})

def cennik_not_logged(request):
    ceny=Cennik.objects.all()
    context={
        'ceny': ceny
        }
    return render(request,"cennik_not_logged.html",context)

# Create your views here.

from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.auth import admin_only


# Create your views here.
@login_required
@admin_only
def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/index.html', context)

def testFunc(request):
    return HttpResponse('this is just the test function')

@login_required
@admin_only
def post_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'product added')
            return redirect('/products/addproduct')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields. ')
            return render(request,'products/addproduct.html',{
                'form':form
            })
    context = {
        'form':ProductForm
    }

    return render(request, 'products/addproduct.html',context)

@login_required
@admin_only
def post_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'category added')
            return redirect('/products/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields. ')
            return render(request,'products/addcategory.html',{
                'form':form
            })
    context = {
        'form':CategoryForm
    }

    return render(request, 'products/addcategory.html',context)

@login_required
@admin_only
def update_product(request,product_id):
    instance = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'product updated')
            return redirect('/products')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields. ')
            return render(request,'products/updateproduct.html',{
                'form':form
            })
    context={
        'form':ProductForm(instance=instance)
    }

    return render(request,'products/updateproduct.html',context)

@login_required
@admin_only
def delete_product(request,product_id):
        product=Product.objects.get(id=product_id)
        product.delete()
        messages.add_message(request,messages.SUCCESS,'product deleted')
        return redirect('/products')



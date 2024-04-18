from django.shortcuts import render,redirect,get_object_or_404
from .models import Product

def delete_product(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    if request.method=="POST":
        product.delete()
        return redirect('all_products')
    return render(request, 'delete_product.html', {'product': product})


def edit_product(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    if request.method=="POST":
        product.name=request.POST.get('name')
        product.price=request.POST.get('price')
        product.launch_date=request.POST.get('launch_date')
        product.save()
        message="Product Created Successfully"
        return redirect('all_products')
    return render(request, 'edit_product.html', {'product': product})

def add_products(request):
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        launch_date=request.POST.get('launch_date')
        Product.objects.create(name=name,price=price,launch_date=launch_date)
        message="Product Created Successfully"
    else:
        message=""
    return render(request, 'add_product.html', {'message': message})

def all_products(request):
    products=Product.objects.all()
    return render(request,"all_products.html",{'products':products})
# Create your views here.

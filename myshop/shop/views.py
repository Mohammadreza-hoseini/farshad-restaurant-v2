from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
import time
from .forms import EmploymentForm
from cart.forms import CartAddProductForm
from .models import Category, Product , Home ,\
    HomeSection1 , HomeSection2 , HomeSection3 , HomeSection4 , ContactusForm
from django.contrib import messages
# Create your views here.


def home(request):
    homeTitle = Home.objects.all()
    homeSection1 = HomeSection1.objects.all()
    homeSection2 = HomeSection2.objects.all()
    homeSection3 = HomeSection3.objects.all()
    homeSection4 = HomeSection4.objects.all()
    if request.method == 'POST':
        contact = ContactusForm()
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact.phone = phone
        contact.subject = subject
        contact.save()
    return render(request,'shop/base.html',{'homeTitle':homeTitle,'homeSection1':homeSection1,'homeSection2':homeSection2,'homeSection3':homeSection3,'homeSection4':homeSection4})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def employment(request):
    if request.POST:
        form = EmploymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ثبت اطلاعات شما انجام شد.در صورت تایید با شما تماس میگیریم.', 'success')
            return redirect('shop:home')
    return render(request, 'shop/product/employment.html', {'form': EmploymentForm()})
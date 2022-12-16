from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):
    return render(request, 'app1/index.html')

def create_views(request):
    context = {}

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, "app1/index.html", context)

def list_view(requset):
    context = {}
    context['dataset'] = Product.objects.all()
    return render(requset, 'app1/seeProduct.html', context)


def update_product(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Product, id=id)

    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/seeProduct/" + str(id))

    # add form dictionary to context
    context["form"] = form
    return render(request, 'app1/Updateproduct.html', context)

def delete_views(request, id):
    obj = get_object_or_404(Product, id=id)
    obj.delete()
    return HttpResponseRedirect('/')

def detail_view(request, id):
    context = {}
    context['data'] = Product.objects.get(id = id)

    return render(request, 'app1/Detailproduct.html', context)

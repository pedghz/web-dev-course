from django.http import HttpResponse, Http404
from webshop.models import Product
# from django.template import loader
from django.shortcuts import render


def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        context = { "product": product, }
        return HttpResponse(render(request, 'webshop/product_view.html', context))
    except:
        raise Http404("There is not such a product in database.")


def available_products(request):
    products = Product.objects.filter(quantity__gt=0)
    context = { "products": products, }
    return HttpResponse(render(request, 'webshop/product_list.html', context))
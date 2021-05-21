from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Address
from .forms import GiveUrl
from django.views.generic import DeleteView

# Create your views here.

def Base_Page(request):
    pricedropped = 0
    Errortype = None

    page = GiveUrl(request.POST or None)

    if request.method == 'POST':
        try:
            if page.is_valid():
                page.save()
        except AttributeError:
            Errortype = "Product Name or Price isn't found!"
        
        except:
            Errortype = "Unknown error!"

    page = GiveUrl()

    query_set = Address.objects.all()
    quantity = query_set.count()

    if quantity > 0:
        flat_price = []
        for item in query_set:
            if item.oldprice > item.currentprice:
                flat_price.append(item)
            pricedropped = len(flat_price)

    context = {
        'query_set': query_set,
        'quantity': quantity,
        'pricedropped': pricedropped,
        'page': page,
        'ErrorType': Errortype, 

    }        

    return render(request, 'Products/main.html', context)

class ProductDelete(DeleteView):
    model = Address
    modal_name = 'Products/deletePage.html'
    success_url = reverse_lazy('Base')

def PriceUpdated(request):
    query_set = Address.objects.all()
    for Products in query_set:
        Products.save()

    return redirect('Base')


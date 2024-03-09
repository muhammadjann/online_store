from django.shortcuts import render,redirect

from item.models import Item, Category
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'market/index.html',
                  {'items': items,
                   'categories': categories})

def contact(request):
    return render(request, 'market/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    form = SignUpForm()
    return render(request, 'market/signup.html', {
        'form':form
    })
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CalcForm, ThingForm
from .models import Account, Things

def home( request):
    account = get_object_or_404( Account, pk=1)
    total = account.total
    context = { 'username': 'Karl Larson', 'total' : total}
    return render( request, 'example/home.html', context)

def calc( request):  
    account = get_object_or_404( Account, pk=1)
    total = account.total
    if request.method == "POST":
        form = CalcForm( request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            action = request.POST['submit']
            if action == "Add":
                account.total = total + amount
            else:
                if amount <= total:
                    account.total = total - amount
                else:
                    print('error: insufficient balance')
            account.save();
            return redirect('/')

    form = CalcForm()
    context = { 'form': form}
    return render( request, 'example/calc.html', context)

def thing( request):  
    if request.method == "POST":
        form = ThingForm( request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            name = form.cleaned_data['name']
            print( amount, name)
            form.save();
            return redirect('/')

    form = ThingForm()
    context = { 'form': form}
    return render( request, 'example/thing.html', context)



def things( request):
    things = Things.objects.all()
    context = { 'things': things}
    return render( request, 'example/things.html', context)
from ctypes import cast
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .form import RawProductionForm, CastForm
from .models import Cast

# Create your views here.


#update
def cast_update_view(request, id=id):
    obj = get_object_or_404(Cast, id=id)
    form = CastForm(request.POST or None, request.FILES or None,  instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "cast/cast_new_form.html", context)

#form to add cast
def cast_add_view(request):
    form = RawProductionForm()
    if request.method == "POST":
        form = RawProductionForm(request.POST, request.FILES)
        if form.is_valid():
            Cast.objects.create(**form.cleaned_data)
        form = RawProductionForm()
    context = {
        'form' : form
    }
    return render(request,'cast/cast_new_form.html', context)

#showing list of cast
def cast_list_view(request):
    queryset = Cast.objects.all()

    context = {
        'object_list' : queryset
    }

    return render(request, 'cast/cast_list.html', context)


#showing cast details
def cast_detail_view(request,id):
    obj = get_object_or_404(Cast, id=id)
    context = {
        "object" : obj 
    }
    return render(request, 'cast/cast_detail.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImagesCreateForm

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImagesCreateForm(data = request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item= form.save(commit=False)

            new_item.user= request.user
            new_item.save()
            messages.success(request, 'Image added')

            return redirect(new_item.get_absolute_url())
    else:
        form =ImagesCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', { 'section': 'images' , 'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImagesCreateForm
from django.shortcuts import get_object_or_404
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
@require_POST
def image_like(request):
    image_id = require_POST.get('id')
    action = require_POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({ 'status':'ok'})
        except:
            pass
    return JsonResponse({ 'status':'ok'})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html',
                  {'section': 'images',
                   'image': image})

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImagesCreateForm(data = request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item= form.save(commit=False)

            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added')

            return redirect(new_item.get_absolute_url())
    else:
        form =ImagesCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', { 'section': 'images' , 'form': form})



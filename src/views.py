# slider_app/views.py
from django.shortcuts import render
from src.models import SliderImage


def slider_view(request):
    slider_images = SliderImage.objects.all().order_by('order')
    return render(request, 'src/slider.html', {'slider_images': slider_images})

from django.forms import models
from django.shortcuts import render
from itertools import chain
from .models import drawing2d3d, printing3d, ProductRendering, Lasercutting, CNCcutting, Sheetmetal, Metalstrture, \
    Furnitureandtoys
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.http import HttpResponse

def home(request):
    all_pics = list(chain(
        drawing2d3d.objects.all(),
        printing3d.objects.all(),
        ProductRendering.objects.all(),
        Lasercutting.objects.all(),
        CNCcutting.objects.all(),
        Sheetmetal.objects.all(),
        Metalstrture.objects.all(),
        Furnitureandtoys.objects.all()
    ))

    for pic in all_pics:
        pic.model_name = pic.__class__.__name__

    return render(request, "index.html", {"all_pics": all_pics})
def designs3D(request):
    pics = drawing2d3d.objects.all()
    model_name = "drawing2d3d"
    return render(request, "3D_designs.html", {"pics": pics, "model_name": model_name})


def printing3D(request):
    pics = printing3d.objects.all()
    model_name = "printing3d"
    return render(request, "printing.html", {"pics": pics, "model_name": model_name})


def Productrendering(request):
    pics = ProductRendering.objects.all()
    model_name = "ProductRendering"
    return render(request, "prorendering.html", {"pics": pics, "model_name": model_name})


def laserplasmacutting(request):
    pics = Lasercutting.objects.all()
    model_name = "Lasercutting"
    return render(request, "laser.html", {"pics": pics, "model_name": model_name})


def cnccutting(request):
    pics = CNCcutting.objects.all()
    model_name = "CNCcutting"
    return render(request, "cnccutting.html", {"pics": pics, "model_name": model_name})

def sheetmetal(request):
    pics = Sheetmetal.objects.all()
    model_name = "Sheetmetal"
    return render(request, "sheet_metal.html", {"pics": pics, "model_name": model_name})

def metalstructuredesigns(request):
    pics = Metalstrture.objects.all()
    model_name = "Metalstrture"
    return render(request, "metal_structure.html", {"pics": pics, "model_name": model_name})

def furnitureandtoys(request):
    pics = Furnitureandtoys.objects.all()
    model_name = "Furnitureandtoys"
    return render(request, "furniture.html", {"pics": pics, "model_name": model_name})

from django.apps import apps

def image_detail(request, model_name, pk):
    app_config = apps.get_app_config('anushka')
    try:
        model_class = app_config.get_model(model_name)
        image = get_object_or_404(model_class, pk=pk)
        return render(request, "image_detail.html", {"image": image})
    except LookupError:
        return render(request, "404.html", status=404)

# email

def send_email(request):
    if request.method == 'POST':

        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        recipient_list = ['amb3dcad.solutions@gmail.com']

        full_message = f"Sender's Name: {subject}\nSender's Email: {from_email}\n\nMessage:\n{message}"

        send_mail(
            subject=f"New Contact Form Submission from {subject}",
            message=full_message,
            from_email='amb3dcad.solutions@gmail.com',
            recipient_list=recipient_list
        )

        return HttpResponse('Email sent successfully')
    else:
        return render(request, 'index.html')

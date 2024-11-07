from django.shortcuts import render
from itertools import chain
from .models import drawing2d3d, printing3d,ProductRendering,Lasercutting, CNCcutting
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


def home(request):
    image_pics = drawing2d3d.objects.all()
    profile_pics = printing3d.objects.all()
    all_pics = list(chain(image_pics, profile_pics))
    return render(request, "index.html", {"all_pics": all_pics})


def designs3D(request):
    pics = drawing2d3d.objects.all()
    return render(request, "3D_designs.html", {"pics": pics})


def printing3D(request):
    pics = printing3d.objects.all()
    return render(request, "printing.html", {"pics_1": pics})


def Productrendering(request):
    pics = ProductRendering.objects.all()
    return render(request, "prorendering.html", {"pics": pics})


def laser(request):
    pics = Lasercutting.objects.all()
    return render(request, "laser.html", {"pics": pics})

def cnc(request):
    pics = CNCcutting.objects.all()
    return render(request, "cnccutting.html", {"pics": pics})

# def LaserPlasma(request):
#     pics_1 = Laserandplasma.objects.all()
#     return render(request, "prorendering.html", {"pics_1": pics_1})


def image_detail(request, model_name, pk):
    # Get the model class based on the model name from the URL
    content_type = get_object_or_404(ContentType, model=model_name)
    model_class = content_type.model_class()

    # Retrieve the image object
    image = get_object_or_404(model_class, pk=pk)

    # Render the template with the retrieved image object
    return render(request, "image_detail.html", {"image": image})


# email
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


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



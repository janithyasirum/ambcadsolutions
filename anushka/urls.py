# from anushka import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include
from .views import home, designs3D,Productrendering, printing3D, cnccutting, \
    laserplasmacutting,cnccutting,sheetmetal,metalstructuredesigns,furnitureandtoys, image_detail, send_email


urlpatterns = [
    path('', views.home, name="home"),
    path('designs3D/', views.designs3D, name="designs3D"),
    path('printing3D', views.printing3D, name="printing3D"),
    path('Productrendering', views.Productrendering, name="Productrendering"),
    path('laserplasmacutting', views.laserplasmacutting, name="laserplasmacutting"),
    path('cnccutting', views.cnccutting, name="cnccutting"),
    path('sheetmetal', views.sheetmetal, name="sheetmetal"),
    path('metalstructuredesigns', views.metalstructuredesigns, name="metalstructuredesigns"),
    path('furnitureandtoys', views.furnitureandtoys, name="furnitureandtoys"),
    path('image-detail/<str:model_name>/<int:pk>/', views.image_detail, name='image_detail'),
    path('send-email/', send_email, name='send_email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
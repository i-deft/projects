from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', views.divisions, name='divisions'),
    path('<slug:division_slug>/', views.division, name='division'),
    path('<slug:division_slug>/<slug:reagent_slug>/', views.reagent, name='reagent')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


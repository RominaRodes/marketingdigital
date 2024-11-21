
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('prueba', views.landing2_view, name='landing2'),
    path('nosotros', views.nosotros_view, name='landing3'),

]

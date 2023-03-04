from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('product/<int:id>',views.product,name='product'),
    path('checkout',views.checkout,name='checkout'),
    path('tracker',views.tracker,name='tracker'),

]
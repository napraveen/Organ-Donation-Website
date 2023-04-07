from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('new',views.new,name='new'),
    path('donors',views.donors,name='donors'),
    path('certificate',views.certificate, name='certificate'),
    path('donate',views.donate,name='donate'),
    path('dummy',views.dummy,name='dummy'),
    path('donors2',views.donors2,name='donors2'),
    path('about',views.about, name='about'),
    path('add/<int:id>',views.add,name='add'),
]
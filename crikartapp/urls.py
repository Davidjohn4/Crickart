from django.urls import path
from crikartapp import views

urlpatterns = [
	path('',views.home,name='indexpage'),
    #path('demo/',views.categor, name='home'),
    path("product/<int:id>", views.product, name="product"),
    ]

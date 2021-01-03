"""crikartsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crikartapp import views
from django.conf import settings 
from django.conf.urls.static import static

admin.site.site_header = "Admin"
admin.site.site_title = "Admin"
admin.site.index_title = "Crikart Database"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('crikartapp.urls')),
    #path('home/',views.home,name='homepage'),
   #path('home/',views.home,name='homepage'),
    path('base/',views.base,name='base'),
    path('final/',views.final,name='final'),
    path('player/',views.player_view,name='playerpage'),
    path('team/',views.team_view,name='teampage'),
    path('category/',views.category,name='categorypage'),
    path('product/',views.product,name='productpage'),
    #path('product/',views.product1,name='productpage'),
    path('cart/',views.cart,name='cartpage'),
    path('checkout/',views.checkout_view,name='checkoutpage'),
    path('about/',views.about,name='aboutpage'),
    path('game/',views.game,name='gamepage'),
    #path('college/',views.college,name='collegepage'),
    path('blog/',views.blog,name='blogpage'),
    path('contact/',views.contact,name='contactpage'),
    #path('feedback/',views.feedback_view,name='feedbackpage'),
    path('register/',views.register, name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.login,name='logout'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                            document_root=settings.MEDIA_ROOT) 

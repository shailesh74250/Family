from django.contrib import admin
from django.urls import path, include
from familysoft import views
# from family import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('about-us', views.aboutUs, name='aboutUs'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('services', views.services, name='services'),
    path('family', include('family.urls')),
    path('FamilySoft-joinus', views.joinus, name='joinus')
]

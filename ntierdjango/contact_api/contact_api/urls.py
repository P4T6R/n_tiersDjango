
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from contacts import views



router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

   
]
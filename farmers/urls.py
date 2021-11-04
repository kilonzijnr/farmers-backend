from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from forum import views
from django.conf.urls.static import static
from django.conf import settings

router=routers.DefaultRouter()
router.register(r'Disease', views.DiseaseViewSet),
router.register(r'Crop', views.CropViewSet)
router.register(r'Farmer', views.FarmerViewSet)
router.register(r'Image', views.ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

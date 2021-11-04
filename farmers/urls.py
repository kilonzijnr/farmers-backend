from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from forum import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views as token_views

router=routers.DefaultRouter()
router.register(r'Disease', views.DiseaseViewSet),
router.register(r'Crop', views.CropViewSet)
router.register(r'Farmer', views.FarmerViewSet)
router.register(r'Image', views.ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-login/', token_views.obtain_auth_token), 
    path('accounts/', include('rest_registration.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

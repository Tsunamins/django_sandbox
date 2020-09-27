from django.contrib import admin
# from django.urls import path
from django.urls import include, path
from rest_framework import routers
from sandbox_api import views


router = routers.DefaultRouter()
# from docs intro to default User and Groups models
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('sandbox_api.urls')),
    # from custom user tutorial
    path('auth/', include('sandbox_api.urls'))


]

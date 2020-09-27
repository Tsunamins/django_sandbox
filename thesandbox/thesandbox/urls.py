from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sandbox_api import views

# this was from docs intro to using default User and Group but can be done differently anyway, and currently not in use
# router = routers.DefaultRouter()
# from docs intro to default User and Groups models
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('sandbox_api.urls')),
    # from custom user tutorial, but sandbox_api.urls already included above
    # if needed to name the register/ path with pre-fix of auth should prefix in app's urls
    # path('auth/', include('sandbox_api.urls'))


]

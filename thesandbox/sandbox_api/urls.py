from django.urls import path

from .views import (
    PuppyListView,
    PuppyDetailView,
    PuppyCreateView,
    PuppyUpdateView,
    PuppyDeleteView,
    # BucketlistListView,
    # BucketlistDetailView,
    # BucketlistCreateView,
    # BucketlistUpdateView,
    # BucketlistDeleteView,
   

)

urlpatterns = [
    path('', PuppyListView.as_view()),
    path('create/', PuppyCreateView.as_view()),
    path('<pk>', PuppyDetailView.as_view()),
    path('<pk>/update/', PuppyUpdateView.as_view()),
    path('<pk>/delete/', PuppyDeleteView.as_view()),
    # path('', BucketlistListView.as_view()),
    # path('create/', BucketlistCreateView.as_view()),
    # path('<pk>', BucketlistDetailView.as_view()),
    # path('<pk>/update/', BucketlistUpdateView.as_view()),
    # path('<pk>/delete/', BucketlistDeleteView.as_view()),
]

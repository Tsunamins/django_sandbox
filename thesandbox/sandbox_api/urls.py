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
    #from custom user tutorial
    RegisterView,
   

)

urlpatterns = [
    path('puppy/', PuppyListView.as_view()),
    path('puppy/create/', PuppyCreateView.as_view()),
    path('puppy/<pk>', PuppyDetailView.as_view()),
    path('puppy/<pk>/update/', PuppyUpdateView.as_view()),
    path('puppy/<pk>/delete/', PuppyDeleteView.as_view()),
    # path('bucketlist/', BucketlistListView.as_view()),
    # path('bucketlist/create/', BucketlistCreateView.as_view()),
    # path('bucketlist/<pk>', BucketlistDetailView.as_view()),
    # path('bucketlist/<pk>/update/', BucketlistUpdateView.as_view()),
    # path('bucketlist/<pk>/delete/', BucketlistDeleteView.as_view()),
    #from custom user tutorial
    path('register/', RegisterView.as_view(), name='register'),
]

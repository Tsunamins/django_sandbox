from django.urls import path

from .views import (
    PuppyListView,
    PuppyDetailView,
    PuppyCreateView,
    PuppyUpdateView,
    PuppyDeleteView
)

urlpatterns = [
    path('', PuppyListView.as_view()),
    path('create/', PuppyCreateView.as_view()),
    path('<pk>', PuppyDetailView.as_view()),
    path('<pk>/update/', PuppyUpdateView.as_view()),
    path('<pk>/delete/', PuppyDeleteView.as_view())
]
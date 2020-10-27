from django.urls import path
from story.views import StoryListView, StoryDetailView

urlpatterns = [
    path('/lists', StoryListView.as_view()),
    path('/details', StoryDetailView.as_view())
]
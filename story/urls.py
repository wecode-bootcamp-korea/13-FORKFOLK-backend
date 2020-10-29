from django.urls import path
from story.views import StoryListView, StoryDetailView

urlpatterns = [
    path("/<int:main_id>", StoryListView.as_view()),
    path("/story/<int:story_id>", StoryDetailView.as_view())
]
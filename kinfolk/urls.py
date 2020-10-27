from django.urls import path, include

urlpatterns = [
    path('my-account',include('user.urls')),
    path('stories', include('story.urls'))
]
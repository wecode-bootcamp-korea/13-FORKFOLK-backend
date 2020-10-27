import json

from django.views import View
from django.http  import JsonResponse, HttpResponse

from story.models import *


class StoryListView(View):
    def get(self, request):
        try:
            main_id_from_front = int(request.GET.get("main_id", None))
            stories            = Story.objects.filter(main_category_id = main_id_from_front)
            story_list         = []
            for one_story in stories:
                story_list.append({
                    "id"        : one_story.id,
                    "title"     : one_story.title,
                    "content"   : one_story.content,
                    "image_url" : StoryImage.objects.filter(story_id = one_story.id)[0].image_url
                    })
            return JsonResponse({"message":"SUCCESS!", "story_list": story_list[:10]}, status=200)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"}, status=400)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"}, status=400)

class StoryDetailView(View):
    def get(self, request):
        try:
            story_id_from_front = int(request.GET.get("story_id", None))
            story               = Story.objects.get(id = story_id_from_front)
            image               = StoryImage.objects.filter(story_id = story_id_from_front).values()
            related_stories     = Story.objects.filter(main_category_id = story.main_category_id)
            story_detail        = []
            related_list        = []
            story_detail.append({
                "id"          : story.id,
                "title"       : story.title,
                "content"     : story.content,
                "description" : story.description,
                "image_url1"  : image[0]['image_url'],
                "image_url2"  : image[1]['image_url'],
                "image_url3"  : image[2]['image_url']
            })
            for related_story in related_stories:
                related_list.append({
                    "id"        : related_story.id,
                    "title"     : related_story.title,
                    "content"   : related_story.content,
                    "image_url" : StoryImage.objects.filter(story_id = related_story.id)[0].image_url
                    })            
            return JsonResponse({"message":"SUCCESS!", "story_detail": story_detail, "related_stories": related_list}, status=200)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"}, status=400)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"}, status=400)
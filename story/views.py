import json
import random

from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse, HttpResponse

from story.models     import MainCategory, SubCategory, Story, StoryImage


class StoryListView(View):
    def get(self, request, main_id):
        try:
            story_list = [{
                "id"        : one_story.id,
                "title"     : one_story.title,
                "content"   : one_story.content,
                "issue"     : SubCategory.objects.get(id = one_story.sub_category_id).name,
                "image_url" : StoryImage.objects.filter(story_id = one_story.id)[0].image_url
            } for one_story in Story.objects.filter(main_category_id = main_id)]
            recycle_stories = [{
                "id"        : recycle_story.id,
                "title"     : recycle_story.title,
                "content"   : recycle_story.content,
                "image_url" : StoryImage.objects.filter(story_id = recycle_story.id)[0].image_url
            } for recycle_story in Story.objects.filter(Q(id__gt=40) & Q(id__lt=61)).order_by('?')[:18]]    
            return JsonResponse({"message":"SUCCESS!", "story_list": story_list[:10], "recycle_stories": recycle_stories}, status=200)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"}, status=400)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"}, status=400)

class StoryDetailView(View):
    def get(self, request, story_id):
        try:
            story               = Story.objects.get(id = story_id)
            image               = StoryImage.objects.filter(story_id = story_id).values()
            story_detail        = []
            story_detail.append({
                "id"          : story.id,
                "title"       : story.title,
                "content"     : story.content,
                "description" : story.description,
                "issue"       : SubCategory.objects.get(id = story.sub_category_id).name,
                "image_url1"  : image[0]['image_url'],
                "image_url2"  : image[1]['image_url'],
                "image_url3"  : image[2]['image_url']
            })
            related_stories = [{
                "id"        : related_story.id,
                "title"     : related_story.title,
                "content"   : related_story.content,
                "image_url" : StoryImage.objects.filter(story_id = related_story.id)[0].image_url
            } for related_story in Story.objects.filter(main_category_id = story.main_category_id).order_by('?')[:6]]          
            return JsonResponse({"message":"SUCCESS!", "story_detail": story_detail, "related_stories": related_stories}, status=200)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"message":"VALUE_ERROR"}, status=400)
        except TypeError:
            return JsonResponse({"message":"TYPE_ERROR"}, status=400)
import json
import math
from itertools import permutations
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import VenueList, Path

class VenueListView(View):
    def post(self, request):
        body = json.loads(request.body)
        venue_list = VenueList.objects.create(venue_list=str(body['venue_list']))
        response = {
            'pk': venue_list.pk
        }
        return HttpResponse(json.dumps(response))

class FindShortestRoutes(View):
    def get(self, request, pk):
        venue_list = VenueList.objects.get(pk=pk)

        shortest = float("inf")
        paths = []

        if not venue_list.paths.exists():

            for p in permutations(venue_list.array[1:]):
                p_list = list(p)
                p_list.insert(0, venue_list.array[0])
                p_list.append(venue_list.array[0])
                dist = calculateDistance(p_list)
                if dist < shortest:
                    shortest = dist
                    paths = [(p_list)]
                elif dist == shortest:
                    paths.append(p_list)

            for p in paths:
                Path.objects.create(path=str(p), distance=shortest, venues_id=venue_list.pk)

        else:
            for p in venue_list.paths.all():
                paths.append(p.array)

        print(paths)
        response = {
            'paths': paths,
            'distance': shortest
        }

        return HttpResponse(json.dumps(response))


def calculateDistance(path):
    distance = 0
    for idx, curr in enumerate(path):
          if idx != 0:
              prev = path[idx-1]
              distance += math.sqrt((curr[0] - prev[0])**2 + (curr[1] - prev[1])**2)
    return distance

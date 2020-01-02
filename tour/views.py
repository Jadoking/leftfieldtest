from django.shortcuts import render

# Create your views here.

class FindShortestRoutes(View):
    def get(self, request):

    response = {}

    return HttpResponse(json.dumps(response))


def calculateDistance(path):
    distance = 0
    for idx, curr in enumerate(path):
          if idx != 0:
              prev = path[idx-1]
              distance += math.sqrt((curr[0] - prev[0])**2 + (curr[1] - prev[1])**2)
    return distance

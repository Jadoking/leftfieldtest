from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^venue_list/$', views.VenueListView.as_view(), name='venuelist'),
    url(r'^tour_path/(?P<pk>\w+)/$', views.FindShortestRoutes.as_view(), name='paths'),
]

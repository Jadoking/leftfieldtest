from django.db import models


class VenueList(models.Model):
    venue_list = models.CharField(max_length=200)

    @property
    def array(self):
        return eval(self.venue_list)

class Path(models.Model):
    venues = models.ForeignKey()
    path = models.CharField(max_length=250)
    distance = models.DecimalField()

from django.db import models


class VenueList(models.Model):
    venue_list = models.CharField(max_length=200)

    @property
    def array(self):
        return eval(self.venue_list)

class Path(models.Model):
    venues = models.ForeignKey(
        'tour.VenueList',
        related_name="paths",
        on_delete=models.CASCADE
    )
    path = models.CharField(max_length=250)
    distance = models.DecimalField(decimal_places=25, max_digits=50)

    @property
    def array(self):
        return eval(self.path)

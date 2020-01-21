from django.db import models
from django.contrib.gis.db import models as geo_models



# Create your models here.
class Address(models.Model):
    EGID = models.IntegerField(default=0)
    EDID = models.IntegerField(default=0)
    GDEKT = models.CharField(max_length = 50, default="")
    GDENR = models.PositiveIntegerField(default=99)
    GDENAME = models.CharField(max_length = 50, default="")
    STRNAME = models.CharField(max_length = 50, default="")
    DEINR = models.CharField(max_length = 50, default="")
    PLZ4 = models.IntegerField(default=-99)
    PLZZ = models.IntegerField(default=-99)
    PLZNAME = models.CharField(max_length = 50, default="")
    GKODE = models.FloatField(default=-99)
    GKODN = models.FloatField(default=-99)
    STRSP = models.CharField(max_length = 2, default="")
    STRNAME_DEINR = models.CharField(max_length = 50, default="")
    COORDINATES = geo_models.PointField( srid = 2056)



    # Returns the string representation of the model.
    def __str__(self):
        return self.name

from django.contrib.gis.db import models

# Create your models here.
class addresses(models.Model):
    EGID = models.AutoField(),
    EDID = models.AutoField(),
    GDEKT = models.CharField(max_length = 50),
    GDENR = models.PositiveIntegerField(),
    GDENAME = models.CharField(max_length = 50),
    STRNAME = models.CharField(max_length = 50),
    DEINR = models.CharField(max_length = 50),
    PLZ4 = models.PositiveIntegerField(),
    PLZZ = models.PositiveIntegerField(),
    PLZNAME = models.CharField(max_length = 50),
    GKODE = models.FloatField(),
    GKODN = models.FloatField(),
    STRSP = models.CharField(max_length = 2),
    STRNAME_DEINR = models.CharField(max_length = 50)
    COORDINATES = models.PointField()



    # Returns the string representation of the model.
    def __str__(self):
        return self.name

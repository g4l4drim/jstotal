from django.db import models
import os
import time
##
# Settup the file name/path with the time and the filename
def threatpath(instance, filename):
        return '/'.join(
                        [
                        os.path.dirname(os.path.abspath(__file__)),
                        'uploads/files',
                         time.strftime("%d/%m/%y"),
                         filename
                         ]
                      )


# Create your models here.
class threattype(models.Model):
    typename = models.CharField(max_length=30)
    def __str__(self):
        return str(u"%s" % self.typename)
    def __unicode__(self):
        return u"%s" % self.typename


class PotentialThreat(models.Model):
    filename = models.CharField(max_length=100)
    sha256 =  models.CharField(max_length=100)
    filetype = models.ForeignKey(threattype)
    threatfile  = models.FileField(upload_to=threatpath, max_length=200)
    submittime = models.DateTimeField(auto_now=True)


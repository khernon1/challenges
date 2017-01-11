from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
import pdb

class Jobs(models.Model):
  job_id = models.IntegerField(default=0)
  agency = models.CharField(max_length=200)
  salary = models.IntegerField(default=0)  
  posting_date = models.DateField(default=timezone.now)
  post_updated = models.DateField(default=timezone.now)

  def __str__(self):
    return str(self.job_id) + ' - ' + str(self.posting_date)




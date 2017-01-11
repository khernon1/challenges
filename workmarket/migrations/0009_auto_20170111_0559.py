# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 05:59
from __future__ import unicode_literals
from django.db import migrations
from string import strip
import pdb

def load_jobs(apps, schema_editor):
  Jobs = apps.get_model("workmarket", "Jobs")
  with open("workmarket/NYC_Jobs_updated.csv", "r") as myfile:
    for line in myfile:      
      split_line = line.split(',')
      split_line = map(strip, split_line)
      if split_line[0] != 'Job ID':
        new_job = Jobs(job_id=split_line[0], 
                      agency=split_line[1], 
                      salary=split_line[2],
                      posting_date=split_line[3],
                      post_updated=split_line[4])
        new_job.save()

class Migration(migrations.Migration):

    dependencies = [
        ('workmarket', '0008_auto_20170111_0549'),
    ]

    operations = [
      migrations.RunPython(load_jobs)
    ]

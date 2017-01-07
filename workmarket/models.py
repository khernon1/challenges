from __future__ import unicode_literals
from django.db import models

class Resume(models.Model):
  char = models.TextField()



  # read in resume 
  #   line by line - add each line to existing array
  #   or as one
  # remove whitespace and punctuation
  # sort

  # show all letter and number count
  # show all letters and numbers that don't exist on it

# from django.db import connection
# from django.conf import settings
# from workmarket import models
from workmarket.models import Jobs

class RunQueries():

  def __init__(self):
    self.my_custom_sql()

  def my_custom_sql(self):
    for p in Jobs.objects.raw("SELECT COUNT(agency) FROM workmarket_jobs"):
      print p

    # settings.configure()
    # with connection.cursor() as cursor:
    #   pdb.set_trace()
    #   cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    #   cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    #   row = cursor.fetchone()
    # return row

RunQueries()
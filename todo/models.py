from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from datetime import date

#ForeignKey: wenn auf anderes Model referenziert wird
class Todo(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  created_at = models.DateField(default=datetime.today)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  def time_passed(self):
    today = date.today()
    delta = today - self.created_at

    return delta.days

  # def user_id(self):
  #   return self.user.id
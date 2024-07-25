from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

#ForeignKey: wenn auf anderes Model referenziert wird
class Todo(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  created_at = models.DateField(default=datetime.today)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
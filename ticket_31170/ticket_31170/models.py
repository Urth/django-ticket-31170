from django.db import models


class Article(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)

from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    food = models.CharField( max_length=100, blank = True, null = True)

    def __str__(self):
        return str(self.food)


class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    comment = models.CharField( max_length=500, blank= True, null = True)


    def __str__(self):
        return str(self.comment)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.reply)


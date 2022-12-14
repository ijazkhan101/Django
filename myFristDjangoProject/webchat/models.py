from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User 

class ChatBoard(models.Model):
    name =models.CharField(max_length=35 , unique=True)
    details= models.CharField(max_length=150)

class ChatTopic(models.Model):
    subject =models.CharField(max_length= 250)
    lastUpdate =models.DateField(auto_now_add =True)
    boardName = models.ForeignKey(ChatBoard,related_name='topics',on_delete=models.CASCADE)
    bordStarter =models.ForeignKey(User,related_name ='topics',on_delete=models.CASCADE)

class Post(models.Model):
    message = models.TextField(max_length = 5000)
    topic = models.ForeignKey(ChatTopic,related_name ='post',on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt =models.DateTimeField(null=True)
    createdBy =models.ForeignKey(User,related_name ='post',on_delete=models.CASCADE)
    updatedBy = models.ForeignKey(User,null= True,related_name ='+',on_delete=models.CASCADE)

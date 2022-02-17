from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import model_to_dict

User= get_user_model()
# Create your models here.
class Blog(models.Model):
    post=models.CharField(max_length=1000)
    date_created= models.DateTimeField(auto_now_add=True)
 
    def __str__(self) -> str:
        return f"{self.post} created {self.date_created}"

# class Like(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='likes')
#     post=models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
#     like=models.BooleanField(default=False)
#     date_added=models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.user
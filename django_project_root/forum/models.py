from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Thread(models.Model):
    subject = models.CharField(max_length=300)
    creator = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.subject)



class Comment(models.Model):
    text = models.TextField()
    thread_id = models.ForeignKey('Thread', related_name='thread', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)




    def __str__(self):
        return str(self.thread_id)


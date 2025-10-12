from django.db import models
from accounts.models import User

# Create your models here.


class VotePoll(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class VoteOption(models.Model):
    poll = models.ForeignKey(VotePoll, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.poll.title} - {self.text}"
    

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(VotePoll, on_delete=models.CASCADE)
    option = models.ForeignKey(VoteOption, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user', 'poll')

    def __str__(self):
        return f"{self.user.username} - {self.option.text}"
    
    


from django.contrib import admin

from polls.apps import PollsConfig
from .models import VotePoll, VoteOption, Vote
# Register your models here.
admin.site.register(VotePoll)
admin.site.register(VoteOption)
admin.site.register(Vote)
admin.site.register(PollsConfig)

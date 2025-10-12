from django.shortcuts import render
from .models import VotePoll, VoteOption, Vote
# Create your views here.

def poll_list(request):
    polls = VotePoll.objects.filter(is_active=True)
    return render(request, 'polls/poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = VotePoll.objects.get(id=poll_id)
    options = VoteOption.objects.filter(poll=poll)
    return render(request, 'polls/poll_detail.html', {'poll': poll, 'options': options})

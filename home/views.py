from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, _get_queryset
from django.views.generic.edit import CreateView
from .models import Question, Player, AnsweredQuestions, PlayerFollowing
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist



def home(request):
    author = request.user.get_username()
    present = False
    present1 = False
    players = Player.objects.all()
    feed = Question.objects.all()
    feed2 = AnsweredQuestions.objects.all()
    for player in players:
        if player.username == author:
            questions = []
            pks = []
            for q in feed:
                if q.player == author:
                    questions.append(q.message)
                    pks.append(q.pk)
            if len(questions) > 0:
                if request.method == "POST":
                    for qu in questions:
                        if request.POST.get(qu):
                            pk = 1
                            for item in feed:
                                if item.message == qu:
                                    pk = item.pk
                            question = Question.objects.get(pk=pk)
                            form1 = AnsweredQuestions(message=question.message, author=question.author, player=author, response=request.POST.get(qu))
                            form1.save()
                            question.delete()
                            questions.remove(qu)
                    if len(questions) > 0:
                        return render(request, "home/playerhome.html", {"feed": questions, "person": author, "present": True})
                    else: 
                        return render(request, "home/playerhome.html", {"a": "No Questions at this time!", "person": author, "present": False})
                else: 
                   return render(request, "home/playerhome.html", {"feed": questions, "person": author, "present": True})
            else: 
                return render(request, "home/playerhome.html", {"a": "No Questions at this time!", "person": author, "present": False})
        else:          
            if request.method == "POST":
                form = Question(message=request.POST.get('message'), author=author, player=request.POST.get('player'), response='Unanswered', answered=False)
                form.save()
            
            return render(request, "home/home.html", {"feed": reversed(feed), "person": author, "feed2": reversed(feed2), "present": True})   
    return render(request, "home/base.html", {"person": author, "feed2": reversed(feed2)})


def roster(request): 
    roster = Player.objects.all()
    try:
        objects = PlayerFollowing.objects.filter(author=request.user)
        if not objects.exists():
            print('no objects')
            for player in roster:
                playerToUpdate = PlayerFollowing(author=request.user, username=player.username, following=False)
                playerToUpdate.save()
    except ObjectDoesNotExist:
        for player in roster:
            playerToUpdate = PlayerFollowing(author=request.user, username=player.username, following=False)
            playerToUpdate.save()
    if request.method == "POST":
        if request.POST.get('update'):
            for player in roster:
                if request.POST.get(player.username):
                    print("Attempting to update: " + str(player.name))
                    try: 
                        playerToUpdate = PlayerFollowing.objects.get(author=request.user, username=player.username)
                        playerToUpdate.following = True
                        playerToUpdate.save()
                        print('Update Complete')
                    except ObjectDoesNotExist:
                        playerToUpdate = PlayerFollowing(author=request.user, username=player.username, following=True)
                        playerToUpdate.following = False
                        playerToUpdate.save()
                        print('New Follow Completed')
                else: 
                    try: 
                        playerToUpdate = PlayerFollowing.objects.get(author=request.user, username=player.username)
                        playerToUpdate.following = False
                        playerToUpdate.save()
                        print('Update Complete')
                    except ObjectDoesNotExist:
                        playerToUpdate = PlayerFollowing(author=request.user, username=player.username, following=True)
                        playerToUpdate.following = False
                        playerToUpdate.save()
                        print('New Follow Completed')
    else:
        pass
    return render(request, "home/roster.html", {"person": request.user.get_username(), "roster": roster, "follows": PlayerFollowing.objects.filter(author=request.user)})
    

def videos(request):
    return render(request, "home/videos.html", {"person": request.user.get_username()})

def calendar(request):
    return render(request, "home/calendar.html", {"person": request.user.get_username()})

def store(request):
    return render(request, "home/store.html", {"person": request.user.get_username()})

def following(request):
    pass


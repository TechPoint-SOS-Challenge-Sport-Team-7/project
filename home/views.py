from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, _get_queryset
from django.views.generic.edit import CreateView
from .models import Question, Player, AnsweredQuestions, UserFollowing, MovieInfo, Item
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
        print("got here")
        if player.username == author:
            print("Player Detected")
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
                            player = players.get(username=author)
                            form1 = AnsweredQuestions(message=question.message, author=question.author, player=author, playerName=player.name, response=request.POST.get(qu))
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
    try:
        following = UserFollowing.objects.filter(author=request.user, following=True)
        if (following.count() == 0):
            return render(request, "home/home.html", {"show": False})
    except ObjectDoesNotExist:
            print('no objects found')
            return render(request, "home/home.html", {"show": False})
    print("FAN VIEW1")
    test = feed.filter(player="")
    test1 = feed2.filter(player="")
    for player in following:
        test = test | feed.filter(player=player.username)
        test1 = test1 | feed2.filter(player=player.username)
        print("TEST: "+str(test))
        if request.method == "POST":
            target = players.get(username=request.POST.get('player'))
            print(target)
            form = Question(message=request.POST.get('message'), author=author, player=request.POST.get('player'), playerName=target.name, response='Unanswered', answered=False)
            form.save()
    return render(request, "home/home.html", {"feed": reversed(test), "person": author, "feed2": reversed(test1), "show": True, "following": following})


def roster(request): 
    roster = Player.objects.all()
    try:
        objects = UserFollowing.objects.filter(author=request.user)
        if not objects.exists():
            print('no objects')
            for player in roster:
                playerToUpdate = UserFollowing(author=request.user, username=player.username, playerName=player.name, following=False)
                playerToUpdate.save()
    except ObjectDoesNotExist:
        for player in roster:
            playerToUpdate = UserFollowing(author=request.user, username=player.username, playerName=player.name,following=False)
            playerToUpdate.save()
    if request.method == "POST":
        if request.POST.get('update'):
            for player in roster:
                if request.POST.get(player.username):
                    print("Attempting to update: " + str(player.name))
                    try: 
                        playerToUpdate = UserFollowing.objects.get(author=request.user, username=player.username)
                        playerToUpdate.following = True
                        playerToUpdate.save()
                        print('Update Complete')
                    except ObjectDoesNotExist:
                        playerToUpdate = UserFollowing(author=request.user, username=player.username, playerName=player.name, following=True)
                        playerToUpdate.following = False
                        playerToUpdate.save()
                        print('New Follow Completed')
                else: 
                    try: 
                        playerToUpdate = UserFollowing.objects.get(author=request.user, username=player.username)
                        playerToUpdate.following = False
                        playerToUpdate.save()
                        print('Update Complete')
                    except ObjectDoesNotExist:
                        playerToUpdate = UserFollowing(author=request.user, username=player.username, playerName=player.name, following=True)
                        playerToUpdate.following = False
                        playerToUpdate.save()
                        print('New Follow Completed')
    else:
        pass
    return render(request, "home/roster.html", {"person": request.user.get_username(), "roster": roster, "follows": UserFollowing.objects.filter(author=request.user)})
    

def videos(request):
    obj=Item.objects.all()
    return render(request, "home/videos.html", {"person": request.user.get_username(), 'obj': obj})


def calendar(request):
    return render(request, "home/calendar.html", {"person": request.user.get_username()})


def store(request):
    return render(request, "home/store.html", {"person": request.user.get_username()})


def settings(request):
    return render(request, "home/settings.html", {"person": request.user.get_username()})


def following(request):
    pass


def drivein(response):
    all_movies = MovieInfo.objects.all()
    return render(response, "home/drivein.html", {'Movies': all_movies})


def confirmation(response):
    if (response.POST):
        login_data = response.POST.dict()
        movie = login_data.get("movieSelect")
        lot = login_data.get("lotSelect")
        adult = login_data.get("adultTickets")
        child = login_data.get("childTickets")
        senior = login_data.get("seniorTickets")
        car = login_data.get("carTickets")
        print(movie, lot)
        if movie == 'select' or lot == 'select':
            return HttpResponse('Not enough information. Go back and make sure all fields are filled out!')
        elif adult == child == senior == car == '0':
            return HttpResponse('Not enough information. Go back and make sure all fields are filled out!')
        else:
            context = {'movie': movie, 'lot': lot, 'adult': adult, 'child': child, 'senior': senior, 'car': car}
            return render(response, "home/confirmation.html", context)
    else:
        return render(response, "base.html")

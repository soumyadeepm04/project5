import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime

from .models import Authorize, Authorized, Events, Favorites, Register, User

# Create your views here.

def index(request):
    upcoming_events = []
    today_events = []
    past_events = []
    upcoming_events.extend(Events.objects.filter(date__gt = datetime.datetime.now().date()))
    today_events.extend(Events.objects.filter(date = datetime.datetime.now().date()))
    past_events.extend(Events.objects.filter(date__lt = datetime.datetime.now().date()))

    return render(request, "capstone/index.html", {
        "upcoming_events":upcoming_events, "today_events":today_events, "past_events":past_events
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")

@login_required
def create_event(request):
    if request.method == "POST":
        owner = request.user
        name = request.POST["name"]
        date = request.POST["date"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        description = request.POST["description"]
        venue = request.POST["venue"]
        Events.objects.create(owner = owner, name = name, date = date, start_time = start_time, end_time = end_time, description = description, venue = venue, registered = 0)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "capstone/create_event.html")

@login_required
def event(request, event_id):
    event = Events.objects.get(pk = event_id)
    if Register.objects.filter(registered_event_id = event_id, registered_user = request.user).exists():
        exists = True
    else:
        exists = False
    comments = Authorized.objects.filter(event_id = event_id)
    registered_users = Register.objects.all()
    if Favorites.objects.filter(event_id = event_id, user_favorite = request.user).exists():
        favorite_exists = True
    else:
        favorite_exists = False
    return render(request, "capstone/event.html", {
        "event":event, "exists":exists, "comments":comments, "request.user":request.user, "registered_users":registered_users, "favorite_exists":favorite_exists
    })

@csrf_exempt
@login_required
def register_event(request, event_id):
    if request.method == 'POST':
        Register.objects.create(registered_event_id = event_id, registered_user = request.user)
        event = Events.objects.get(pk = event_id)
        event.registered = event.registered + 1
        event.save()
        return HttpResponse(status = 204)

@csrf_exempt
@login_required
def unregister_event(request, event_id):
    if request.method == 'POST':
        Register.objects.get(registered_event_id = event_id, registered_user = request.user).delete()
        event = Events.objects.get(pk = event_id)
        event.registered = event.registered - 1
        event.save()
        return HttpResponse(status = 204)

@csrf_exempt
@login_required
def comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event_id = data["event_id"]
        comment = data["comment"]
        event_owner = Events.objects.get(pk = event_id).owner
        Authorize.objects.create(event_id = event_id, comment = comment, event_owner = event_owner)
        return HttpResponse(status = 204)

@login_required
def authorize_comments(request):
    comments_to_authorize = Authorize.objects.filter(event_owner = request.user)
    comments_user = Authorize.objects.filter(event_owner = request.user)
    comment_event_ids = []
    for comment_user in comments_user:
        comment_event_ids.append(comment_user.event_id)
    comment_events = []
    for comment_event_id in comment_event_ids:
        comment_events.extend(Events.objects.filter(pk = comment_event_id))
    return render(request, "capstone/authorize_comments.html", {
        "comments_to_authorize":comments_to_authorize, "comment_events":comment_events
    })

@csrf_exempt
@login_required
def authorize(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        event_id = data["event_id"]
        comment = data["comment"]
        Authorized.objects.create(event_id = event_id, comment = comment)
        Authorize.objects.get(event_id = event_id, comment = comment).delete()
        return HttpResponse(status = 204)

@csrf_exempt
@login_required
def reject(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        event_id = data["event_id"]
        comment = data["comment"]
        Authorize.objects.get(event_id = event_id, comment = comment).delete()
        return HttpResponse(status = 204)

@csrf_exempt
@login_required
def edit(request, event_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        event = Events.objects.get(pk = event_id)
        event.name = data["name"]
        event.date = data["date"]
        event.start_time = data["start_time"]
        event.end_time = data["end_time"]
        event.description = data["description"]
        event.venue = data["venue"]
        event.save()
        return HttpResponse(status = 204)

@csrf_exempt
@login_required
def favorite(request, event_id):
    Favorites.objects.create(event_id = event_id, user_favorite = request.user)
    return HttpResponse(status = 204)

@csrf_exempt
@login_required
def unfavorite(request, event_id):
    Favorites.objects.get(event_id = event_id, user_favorite = request.user).delete()
    return HttpResponse(status = 204)

@login_required
def favorite_events(request):
    favorite_objects = Favorites.objects.filter(user_favorite = request.user)
    event_ids = []
    for favorite_object in favorite_objects:
        event_ids.append(favorite_object.event_id)
    
    favorite_events = []
    for event_id in event_ids:
        favorite_events.extend(Events.objects.filter(pk = event_id))

    upcoming_events = []
    today_events = []
    past_events = []
    for favorite_event in favorite_events:
        if favorite_event.date > datetime.datetime.now().date():
            upcoming_events.append(favorite_event)
        elif favorite_event.date == datetime.datetime.now().date():
            today_events.append(favorite_event)
        else:
            past_events.append(favorite_event)
    
    return render(request, "capstone/index.html", {
        "upcoming_events":upcoming_events, "today_events":today_events, "past_events":past_events, "favorite":True
    })
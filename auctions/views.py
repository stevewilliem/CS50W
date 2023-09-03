from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *

# class listingForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea)
#     bid_value =  forms.DecimalField(decimal_places=2)
#     image = forms.URLField(label='Image link', required = False)
#     category = forms.CharField(max_length=40)

def index(request):
    #title, description, current price, photo
    return render(request, "auctions/index.html",{
        "listings" : auction.objects.all()
    })

def listingPage(request, id):
    return render(request, "auctions/listing.html",{
        "listing" : auction.objects.get(pk=id) #pk stands for primary key
    })

def createListing(request):
    if request.method == "POST":
        
        form = listingForm(request.POST)
        if form.is_valid():
            title_id = form.cleaned_data['title']
            description_id = form.cleaned_data['description']
            bid = form.cleaned_data['bid_value']
            # img_url = form.cleaned_data['image']
            cat = form.cleaned_data['category'] 

            listing = auction(title = title_id, 
                              description = description_id,
                              bid_value = bid,
                            #   image = img_url,
                              image = forms.ImageField(),
                              category = cat,
                              active_status = True,
                              creator_id = request.user
                              )

            listing.save()

            print("listing saved")
        else:
            print("form invalid")
            #   If the form is invalid, re-render the page with existing information.
            return render(request, "auctions/createListing.html", {
                "form": form,
            })
    
    return render(request, "auctions/createListing.html", {
    "form": listingForm()
    })

def categories(request):
    return render(request, "auctions/categories.html"
    )

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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

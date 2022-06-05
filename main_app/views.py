from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):


    template_name ="home.html"
    # Here we are adding a method that will be ran when we are dealing with a GET request
    #def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        #return HttpResponse("Finch Home")

class Finch:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


Finches = [
    Finch("Purple Finch", 
    "https://www.allaboutbirds.org/guide/assets/og/75714071-1200px.jpg",
    "sparrow dipped in raspberry juice"),
    Finch("Gouldian Finch", 
    "https://upload.wikimedia.org/wikipedia/commons/3/3e/Male_adult_Gouldian_Finch.jpg",
    "Rainbow"),
    Finch("Zebra Finch", 
    "https://lafeber.com/pet-birds/wp-content/uploads/2018/06/Zebra-Finch.jpg",
    "Seed Eaters")
]


class FinchList(TemplateView):
    template_name = "finches_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finches"] = finches # this is where we add the key into our context object for the view to use
        return context

#...
class About(TemplateView):
     template_name = "about.html"


   # def get(self, request):
        #return HttpResponse("Finch About")
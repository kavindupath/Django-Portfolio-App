from django.shortcuts import render

# Create your views here.

def hello_world_function(request):
    return render(request, "hello_world_view.html", {})
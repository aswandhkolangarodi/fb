from django.shortcuts import render

# Create your views here.
def fblogin(req):
    return render(req,"fb.html")

from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Profile    


#AJAX example
def profile(request):
    return render(request,'profile.html')

def getprofile(request):
    profile = Profile.objects.all()
    return JsonResponse({'profile':list(profile.values())})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']
        new_user = Profile(name=name, email=email, bio=bio)
        new_user.save()
        return HttpResponse('new data created successfully')






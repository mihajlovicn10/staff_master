from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import CheckInOut
from datetime import datetime
from authentication.models import User
from django.contrib.auth.decorators import login_required





#def main(request): 
#    return render(request,"mainpage.html")
@login_required
def faq(request): 
    return render(request,"faq.html")
@login_required
def contact_form(request): 
    return render(request,"contact.html")

@login_required
def check_in(request):
    user = request.user
    last_check_in = CheckInOut.objects.filter(user=user).last()
    checked_in = True if last_check_in else False
    checked_out = False
    if checked_in:
        checked_out = True if last_check_in.check_out else False
        if checked_out:
            checked_in = False

    if request.method == "POST": 
        check_in_out = CheckInOut(user = user, check_in = datetime.now())
        check_in_out.save()
        return redirect("/check_in/")
    return render(request, "mainpage.html", context = {"checked_in":checked_in, "checked_out":checked_out})
@login_required
def check_out(request):
    last_check_in = CheckInOut.objects.all().last()
    last_check_in.check_out = datetime.now()
    last_check_in.save()
    return redirect("/check_in/")

@login_required
def profile(request): 
    user = request.user
    check_in_outs = CheckInOut.objects.filter(user = user).all()
    return render(request,"profile.html", context={"user": user, "check_in_outs": check_in_outs})

   



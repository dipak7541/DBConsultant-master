from django.shortcuts import render, redirect
from core.models import ContactModel


# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        concerntype = request.POST.get("concerntype")
        phone_no = request.POST.get("phone_no")
        message = request.POST.get("message")

        user_message = ContactModel(name=name, email=email, concerntype=concerntype, phone_no=phone_no, message=message)
        user_message.save()
        return redirect('/')

    return render(request, 'main.html')

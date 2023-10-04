from django.shortcuts import render
from .utils import gen_email

def home(request):
    return render(request, "home.html")

def email(request):
    length = int(request.POST.get("length"))
    domain = request.POST.get("domain")
    numeric = request.POST.get("numeric")

    email_gen = gen_email(length, domain, numeric)

    return render(request, "email.html", {"email": email_gen})
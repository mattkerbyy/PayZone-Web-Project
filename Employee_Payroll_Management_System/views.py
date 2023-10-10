from django.shortcuts import render


def home(request):
    return render(request, "home_page/home_web.html", {})

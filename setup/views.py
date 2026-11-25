from django.shortcuts import render


def home(request):
    pessoa = {
        "nome": "Ana",
        "idade": 30,
        "cidade": "São Paulo",
    }
    return render(request, "home.html", {"pessoa": pessoa})


def about(request):
    frutas = ["maçã", "banana", "uva", "laranja"]
    return render(request, "about.html", {"frutas": frutas})
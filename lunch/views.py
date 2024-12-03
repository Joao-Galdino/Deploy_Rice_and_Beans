from django.shortcuts import render

def index(request):
    context = {
        "message": "Bem-vindo ao Feijão com Arroz do Deploy!",
        "env": request.GET.get("env", "Development")
    }
    return render(request, "lunch/index.html", context)
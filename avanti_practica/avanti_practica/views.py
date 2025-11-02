from django.shortcuts import render

def inicio(request):
    return render(request, "index.html")

def acerca(request):
    return render(request, "acerca.html")

def login(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email and password:
            context["mensaje"] = f"Bienvenido, {email}!"
        else: 
            context["mensaje"] = f"Debe completar ambos campos!"
    # ESTO HABIA CAMBIADO
    return render(request, "login.html", context)

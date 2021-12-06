from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            asunto=request.POST.get("asunto")
            mensaje=request.POST.get("mensaje")

            email=EmailMessage(asunto, "Nombre: {}\nCorreo: {}\nMensaje: {}\n\n"
            .format(nombre,email,mensaje,asunto),"",["sagatechsoluciones@gmail.com"],reply_to=[email])

            try:
                email.send()
            
                return redirect("/contact/?valido")
            except:
                return redirect("/contact/?novalido")


    return render(request, 'contact.html', {'miFormulario':formulario_contacto})
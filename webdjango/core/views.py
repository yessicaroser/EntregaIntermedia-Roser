from django.shortcuts import render, HttpResponse


# Create your views here.
html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

def home(request):
    return render(request, "core/home.html")


def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Yessica </p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Te brindamos nuestro email y redes sociales para que puedas contactarnos:</p>
        <ul>
            <li><a href="mailto:hola@cuentafalsa.com.ar.">Email</a></li>
            <li><a href="https://github.com/lisasimpson">Github</a></li>
            <li><a href="https://youtube.com">Youtube</a></li>
        </ul>
    """)

from django.shortcuts import render, HttpResponse

def home(request):
     return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")
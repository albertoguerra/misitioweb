# Create your views here.

from django.core.paginator import Paginator,InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from blog.models import *

from django.forms import ModelForm
from django.core.context_processors import csrf

class FormularioComentario(ModelForm):
    class Meta:
        model = Comentario
        exclude =["identrada"]
        

def poncomentario(request,pk):
    p = request.POST
    if 'mensaje' in p:
        autor = "Anonimo"
        if p["autor"]: autor = p["autor"]

        comentario = Comentario(identrada = Entrada.objects.get(pk=pk))
        cf = FormularioComentario(p,instance = comentario)
        cf.fields['autor'].requiered = False
        
        comentario = cf.save(commit= False)
        comentario.autor= autor
        comentario.save()
    return HttpResponseRedirect(reverse("blog.views.entrada",args=[pk]))

def entrada(request, pk):
    identrada=Entrada.objects.get(pk=int(pk))
    comentario=Comentario.objects.filter(identrada=identrada)
    d=dict(entrada=identrada,comentario=comentario,form=FormularioComentario(),usuario=request.user)
    d.update(csrf(request))
    return render_to_response("entrada.html",d)
    

def main(request):
    entrada = Entrada.objects.all().order_by("-fecha")
    paginator=Paginator(entrada,3)

    try: pagina = int(request.GET.get("page",'1'))
    except ValueError: pagina = 1

    try:
        entrada=paginator.page(pagina)
    except (Invalidpage, EmptyPage):
        entrada= paginator.page(paginator.num_pages)

    return render_to_response("listado.html",dict(entrada = entrada, usuario=request.user))

from django.shortcuts import render
from django.http import HttpResponse
import csv
from django.views.generic.edit import FormView
from leitor_pdf.form import Anexa_arquivo
from leitor_pdf.utils import leitura_upload
from leitor_pdf.models import Constituicao

# Create your views here.

class PdfView(FormView):

    template_name =  'anexa_arquivo.html'
    form_class = Anexa_arquivo
    
    def post (self,request):      
        extraido = leitura_upload(request.FILES['pdf'])
        for lei in extraido:
            Constituicao.objects.create(
                titulo=lei['titulo'],
                capitulo=lei['capitulos'],
                secao=lei['secoes'],
                subsecao=lei['subsecoes'],
                trecho=lei['trecho'],
                pagina_inicial=lei['pagina_inicio'])
       
        constituicao= Constituicao.objects.all() 
            
        return render(request,'resultado.html',{'leis':constituicao})
            

def gerar_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="constituicao.csv"'

    constituicao=Constituicao.objects.all()
    escreva = csv.writer(response)
    escreva.writerow(['Título','Capítulo','Seção','Subseção','Pagina Inicial'])
    for registro in constituicao:
        escreva.writerow([registro.titulo,registro.capitulo,registro.secao,registro.subsecao,registro.pagina_inicial])
    
    

    return response
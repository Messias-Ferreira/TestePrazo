from django.urls import path
from leitor_pdf.views import PdfView,gerar_csv

urlpatterns = [
    path('',PdfView.as_view()),
    path('gerarcsv',gerar_csv, name='gerarCSV')
]
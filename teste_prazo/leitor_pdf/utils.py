from PyPDF2 import PdfFileReader

def leitura_upload(path):

    
    with open(path.file.name,'rb') as f :
        pdf = PdfFileReader(f)

        leis =[]
        texto_titulo = []
        for pagina in range(11,138):    
            pagina_lida = pdf.getPage(pagina)
            linhas_atual = pagina_lida.extractText().split('\n')

            proxima_pagina = pdf.getPage(pagina+1)
            linhas_proximas = proxima_pagina.extractText().split('\n')

            if linhas_atual[0].find('TÍTULO') != -1:
                texto_titulo = linhas_atual
            else:
                texto_titulo =texto_titulo+linhas_atual
            if linhas_proximas[0].find('TÍTULO') != -1: 
                lei = {
                    'titulo' : '',
                    'capitulos' : [],
                    'secoes' : [],
                    'subsecoes' : [],
                    'trecho': '',
                    'pagina_inicio':0,
                    'trecho':'',
                }

                for linha in texto_titulo:
                    linha_atual = texto_titulo.index(linha)
                    lei['trecho'] = lei['trecho'] + linha.replace(' Œ  ','-')
                    if linha.find('TÍTULO')!= -1:
                        lei['titulo'] = linha + texto_titulo[linha_atual+1].replace(' Œ  ','-')
                        lei['pagina_inicio']=pagina -1
                    if linha.find('CAPÍTULO')!= -1:
                        capitulo = '{}-{}'.format(linha,texto_titulo[linha_atual+1].replace(' Œ  ',''))
                        lei['capitulos'].append(capitulo)
                    if linha.find('SEÇÃO') != -1:
                        secao = '{}-{}'.format(linha,texto_titulo[linha_atual+1].replace(' Œ  ',''))
                        lei['secoes'].append(secao)
                    if linha.find('SUBSEÇÃO')!= -1:
                        subsecao = '{}-{}'.format(linha,texto_titulo[linha_atual+1].replace(' Œ  ',''))
                        lei['subsecoes'].append(subsecao)
                leis.append(lei)
    return leis            

                    
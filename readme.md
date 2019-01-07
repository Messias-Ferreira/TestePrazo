# Teste de Leitor De PDF

# Manual de instalação:

## Com o Projeto Clonado Faça:

1. Primeiro passo criar uma VirtualEnv para instalar as dependência do projeto :

    - python3 -m venv *nome_da_env* 

2. Instalar as dependência do projeto :

    - pip install -r requirements.txt 

*obs: O arquivo requirements.txt será encontrado na pasta raiz do projeto*

3. Dentro do Arquivo Clonado entrar na pasta TestePrazo é execultar o seguinte comando :

    - python3 manager.py runserver _porta que preferir_

    *obs: por padrão ele roda na porta 8000*

4. Com o servidor local rodando entrar no Google Chrome para execultar o projeto digitando o seguinte caminho:

    - localhost:8000 *(padrão)* ou a sua porta definida no passo anterior 

Com os passos anteriores realizado com sucesso utilzação do sistema


## Manual de utilização:


1. Enviando PDF *constituicao_brasileira_1998.pdf*

    - Na tela inicial ter um campo para envio de PDF ,selecionar o arquivo *constituicao_brasileira_1998.pdf*

2. Com o PDF enviado ele irá mostrar todos os titulos scanneados/
    - Ao clickar no *titulo* ele irá mostrar os atributos daquel titulo(capítulos,seção,subseção)/

    - Ao Clickar em *Ler trecho* ele mostrará o trecho daquele titulo

    - Clickando em *Gerar CSV* ele baixará um csv para a maquina 




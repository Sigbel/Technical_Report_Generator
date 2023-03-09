<p align="center">
 <img border="5px" width="300px" src="https://res.cloudinary.com/sigbel/image/upload/v1677529248/projects/technical_report_generator/technical_report-figure_khmy1p.gif" align="center" alt="Entrance" />
 <h2 align="center">Technical Report Generator</h2>
 <p align="center">Um gerador de relatórios técnicos em PDF, focado em segurança e bem-estar no trabalho.</p>
</p>

<p align="center">
<a href="https://github.com/Sigbel/Technical_Report_Generator/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/sigbel/Technical_Report_Generator?color=0088ff" />
</a>
<a href="https://github.com/Sigbel/Technical_Report_Generator/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/sigbel/Technical_Report_Generator?color=0088ff" />
</a>

</p>
<p align="center">
<a href="#demonstrativo">Ver demonstração</a>
·
<a href="https://github.com/Sigbel/Technical_Report_Generator/issues/new">Reportar erros</a>
·
<a href="https://github.com/Sigbel/Technical_Report_Generator/issues/new">Solicitar recursos</a>
</p>

# Tópicos

- [Cuidados Iniciais](#cuidados-iniciais)
- [Interfaces](#interfaces)
- [Funcionalidades](#funcionalidades)
- [Observações](#observações)
- [Demonstrativo](#demonstrativo)

## Cuidados Iniciais

Antes de prosseguir com a utilização do aplicativo, certifique-se de instalar todas as dependências presentes no arquivo **requirements.txt**.

## Interfaces

- Cadastro de Clientes
    - Guia para o cadastro de informações prioritárias a respeito dos clientes, tais como razão social, cnpj, endereço, grau de risco, nº de funcionários e ramo de atividade.

- Relatório
    - Guia para edição do relatório final com base no template fornecido (vide [obervações](#observações)).

## Funcionalidades

- Cadastro e edição de clientes
- Criação e edição recursos de relatórios (PDF), tais como: 
    - Escolha do cliente cadastrado no banco de dados
    - Alteração da data do relatório
    - Edição de cabeçalho
    - Edição de campos importantes do relatório (Objetivos, Equip. de Medição, Metodologia, Procedimento)
    - Adição de avaliações ao final do relatório

## Observações

Toda criação de PDFs é feita com base em um modelo pré-estabelecido fornecido em ```report_creator > report_template.py```, caso necessário alterar o template todos os recursos devem ser inseridos na pasta ```images```, respeitando as devidas proporções. O **footer** deve manter as proporções de uma folha **A4**, já a **logo** não possui uma dimensão fixa, porém, é recomendável assim como o footer, respeitar as dimensões de uma folha **A4**.

## Demonstrativo

|<b>_Figura 1 - Guia de Cadastro de Clientes_</b>|
|:--:|
|![img_1.png](https://res.cloudinary.com/sigbel/image/upload/v1677534295/projects/technical_report_generator/cadastro_clientes_snhgbw.png)|

|<b>_Figura 2 - Guia de Edição de Relatório_</b>|
|:--:|
|![img_2.png](https://res.cloudinary.com/sigbel/image/upload/v1677534296/projects/technical_report_generator/report_pdf_wyjick.png)|

|<b>_Figura 3 - Adição de Avaliações_</b>|
|:--:|
|![img_3.png](https://res.cloudinary.com/sigbel/image/upload/v1677534295/projects/technical_report_generator/avaliations_vfmkhz.png)|

|<b>_Figura 4 - Exemplo de Relatório (Logo)_</b>|
|:--:|
|![img_4.png](https://res.cloudinary.com/sigbel/image/upload/v1677534122/projects/technical_report_generator/teste1_page-0001_dkukdr.jpg)|

|<b>_Figura 5 - Exemplo de Relatório (Avaliações)_</b>|
|:--:|
|![img_5.png](https://res.cloudinary.com/sigbel/image/upload/v1677534122/projects/technical_report_generator/teste1_page-0003_pasutx.jpg)|

_Nota: Todos os dados contidos nas imagens são fictícios, sendo meramente representados com a finalidade de ilustrar o funcionamento do aplicativo._

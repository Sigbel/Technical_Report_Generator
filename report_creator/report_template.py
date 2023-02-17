import sqlite3

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime
# from report_creator.texts_test import texts

WIDTH = 210
HEIGHT = 297

class PagesPDFGenerator(Canvas):
    def __init__(self, avaliations, cap, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.avlts = avaliations
        self.cap = cap
        self.client_name = client
        self.pages = []
        self.avlt_count = 0
        self.dt = datetime.now()

        if self.cap == '':
            self.cap = 'Análise Ergonômico Preliminar (AEP)'

        # DataBank Consult and Adaptation
        self.con = sqlite3.connect('./data.db')
        self.cur = self.con.cursor()

        self.cur.execute("SELECT obj, equip, methods, proc FROM report")
        self.texts = self.cur.fetchall()
        
        self.cur.close()

        self.new_texts = []
        for i in range(len(self.texts[0])):
            new = self.texts[0][i].replace('\n', '<BR />\n')
            self.new_texts.append(new)

    def showPage(self):
        self.drawImage("./images/footer.png", 0, 0, WIDTH*mm, HEIGHT*mm, mask='auto')
        self.setFont('Times-Bold', 8)
        self.drawString(10*mm, 286*mm, self.cap)
        
        if len(self.pages) == 0:
            self.drawImage("./images/logo_lux2.jpg", ((WIDTH*mm)/2)-(145*mm/2), ((HEIGHT*mm)/2)-(215*mm/2), 145*mm, 215*mm)
            p = Paragraph(self.client_name, ParagraphStyle(
                name='Logo Style',
                fontName='Times-Roman',
                leading=12,
                alignment=TA_CENTER
            ))
            p.wrapOn(self, 200, 40)
            p.drawOn(self, 71*mm, 145*mm)
        
            p = Paragraph(self.dt.strftime("%d-%m-%Y"), ParagraphStyle(
                name="Date Style",
                fontName='Times-Roman',
                leading=12,
                alignment=TA_CENTER
            ))
            p.wrapOn(self, 200, 40)
            p.drawOn(self, 71*mm, 134*mm)


        elif len(self.pages) == 1:
            self.setFont('Times-Bold', 10)
            self.drawString(27*mm, 265*mm, f'OBJETIVOS')
            p = Paragraph(f'{self.new_texts[0]}', ParagraphStyle(
                    name='Dimensions Style',
                    fontName='Times-Roman',
                    leading=12,
            ))
            p.wrapOn(self, 458, 50)
            p.drawOn(self, 27*mm, 253*mm)

            self.setFont('Times-Bold', 10)
            self.drawString(27*mm, 242*mm, f'EQUIPAMENTOS DE MEDIÇÃO')
            p = Paragraph(f'{self.new_texts[1]}', ParagraphStyle(
                    name='Dimensions Style',
                    fontName='Times-Roman',
                    leading=12,
            ))
            p.wrapOn(self, 458, 50)
            p.drawOn(self, 27*mm, 225*mm)

            self.setFont('Times-Bold', 10)
            self.drawString(27*mm, 214*mm, f'METODOLOGIA')
            p = Paragraph(f'{self.new_texts[2]}', ParagraphStyle(
                    name='Dimensions Style',
                    fontName='Times-Roman',
                    leading=12,
            ))
            p.wrapOn(self, 458, 50)
            p.drawOn(self, 27*mm, 196*mm)

            self.setFont('Times-Bold', 10)
            self.drawString(27*mm, 185*mm, f'PROCEDIMENTO')
            p = Paragraph(f'{self.new_texts[3]}', ParagraphStyle(
                    name='Dimensions Style',
                    fontName='Times-Roman',
                    leading=12,
            ))
            p.wrapOn(self, 458, 50)
            p.drawOn(self, 27*mm, 162*mm)
                
        else:
            self.setFont('Times-Bold', 12)
            self.drawString(27*mm, 265*mm, f'AVALIAÇÃO {self.avlt_count+1}')

            p = Paragraph(f'''
                Dimensão da Sala(m²): <b>{self.avlts[self.avlt_count][0]}</b><br/>
                Tipo de Atividade: <b>{self.avlts[self.avlt_count][1]}</b><br/>
                Nome do Colaborador: <b>{self.avlts[self.avlt_count][2]}</b><br/>
                Tipo de Função: <b>{self.avlts[self.avlt_count][3]}</b><br/><br/>
                Valor de Referência para a Estação: <b>{self.avlts[self.avlt_count][4]}</b>
                ''', ParagraphStyle(
                    name='Dimensions Style',
                    fontName='Times-Roman',
                    leading=12,
            ))

            p.wrapOn(self, 458, 50)
            p.drawOn(self, 27*mm, 234*mm)

            self.line(27*mm, 231*mm, 190*mm, 231*mm)
            self.setFont('Times-Bold', 12)
            self.drawCentredString(108.5*mm, 225*mm, f'AMBIENTE {self.avlt_count+1} - {self.avlts[self.avlt_count][7]}')
            self.line(27*mm, 222*mm, 190*mm, 222*mm)

            self.setFont('Times-Bold', 9)
            self.drawString(47*mm, 216*mm, 'Iluminância na área da tarefa (lux)')
            self.drawString(117*mm, 216*mm, 'Iluminância no entorno imediato (lux)')

            self.line(27*mm, 213*mm, 190*mm, 213*mm)

            if float(self.avlts[self.avlt_count][5]) < float(self.avlts[self.avlt_count][4])*0.9:
                self.setFillColor('red')
            else:
                self.setFillColor('green')
            self.drawString(67*mm, 208*mm, f'{self.avlts[self.avlt_count][5]}')

            self.setFillColor('black')
            self.drawString(137*mm, 208*mm, f'{self.avlts[self.avlt_count][6]}')
            self.line(27*mm, 205*mm, 190*mm, 205*mm)

            # Observation Section
            p = Paragraph(f'''<b>OBSERVAÇÃO:</b><br/><br/>
                {self.avlts[self.avlt_count][8]}<br/><br/>
                ''', ParagraphStyle(
                    name='Obs Style',
                    fontName='Times-Roman',
                    leading=12,
                    borderColor='#000000',
                    borderPadding=(0,2,10),
                    borderWidth=1,
            ))

            p.wrapOn(self, 458, 50)
            p.drawOn(self, 28*mm, 170*mm)

            self.avlt_count += 1
            
        self.rect(10,10, (WIDTH*mm)-20, (HEIGHT*mm)-20)
        self.pages.append(dict(self.__dict__))
        self._startPage()
    
    def save(self):
        page_count=len(self.pages)

        for page in self.pages:
            self.__dict__.update(page)
            self.draw_page_number(page_count)
            super().showPage()

        super().save()

    def draw_page_number(self, page_count):
        page = f"{self._pageNumber}"
        self.setFillColor("gray")
        self.rect(180*mm,284.25*mm, 100, 15, 0, fill=1)
        self.setFillColor("white")
        self.setFont("Helvetica", 9)
        self.drawRightString(185*mm, 286*mm, page)


if __name__ == '__main__':
    avaliations = {
        '1': ['10', 'Administrativo', 'Algusto Fernandes', 'Assistente Administrativo', 500, 170, 410, "Financeiro Administrativo", "Observações 1"],
        '2': ['20', 'Administrativo', 'Maria Ribeiro', 'Secretária (o) executiva (o)', 500, 286, 355, "Secretariado", "Observações 2"],
    }

    c = PagesPDFGenerator(avaliations, 'test.pdf', pagesize=A4)
    c.showPage()
    c.showPage()
    c.showPage()
    c.showPage()
    c.save()
    
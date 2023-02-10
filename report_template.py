from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

WIDTH = 210
HEIGHT = 297


class PagesPDFGenerator(Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = []

    def showPage(self):
        c.drawImage("./images/footer.png", 0, 0, WIDTH*mm, HEIGHT*mm, mask='auto')

        if len(self.pages) == 0:
            text = "Análise Ergonômico Preliminar (AEP)"
            c.drawImage("./images/logo_lux2.jpg", ((WIDTH*mm)/2)-(145*mm/2), ((HEIGHT*mm)/2)-(215*mm/2), 145*mm, 215*mm)
            c.drawString(10*mm, 286*mm, text)

        elif len(self.pages) == 1:
            pass
        
        c.rect(10,10, (WIDTH*mm)-20, (HEIGHT*mm)-20)
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
    c = PagesPDFGenerator('test.pdf', pagesize=A4)
    c.showPage()
    c.showPage()
    c.save()
    
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4

WIDTH, HEIGHT=A4

class ParagraphsCreator():
    def __init__(self, path):
        self.path = path
        self.initial_h = 150
        self.max_h = 820

    def define_style(self, *args, **kwargs):
        style=ParagraphStyle(*args, **kwargs)    
        
        return style

    def define_paragraph(self, text, style):
        p = Paragraph(text, style)
        
        p.wrapOn(self.path, 420, 50)

        p.drawOn(self.path, WIDTH-520, HEIGHT-self.initial_h)
        self.initial_h += 120


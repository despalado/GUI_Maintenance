from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfgen import canvas
# add font
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import subprocess # to open the pdf file

class Report_pdf(object):
    #Constructor of the class
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.width, self.height = A4
    #Method to create the pdf
    def create_pdf(self, filename, data):
        self.doc = SimpleDocTemplate(filename, pagesize=A4, leftmargin=30,
                                     rightmargin=30, topmargin=50, bottommargin=10)
        self.story = [Spacer(1, 1*cm)]
        self.createTable(data)
        self.doc.build(self.story, onFirstPage=self.createDocument)

        print(f"PDF created:{filename}")
    
    #Method to create the coordinate

    def createCoordinate(self, x, y, unit=1):
        x, y = x * unit, self.height -  y * unit
        return x, y
    
    #Method to create document
    def createDocument(self, canvas, doc):
        pdfmetrics.registerFont(TTFont('boldFont', 'Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'Arial Bold.ttf'))

        self.c = canvas
        normal = self.styles["Title"]
        htext ="<font size=18 name='Arial-Bold'> Gamplan </font>"
        h = Paragraph(htext, normal)
        h.wrapOn(self.c, self.width, self.height)
        h.drawOn(self.c, *self.createCoordinate(0, 12, mm))

        htext ="<font size=18 name='boldFont'> Internation CompanyLtd </font>"
        h = Paragraph(htext, normal)
        h.wrapOn(self.c, self.width, self.height)
        h.drawOn(self.c, *self.createCoordinate(0, 20, mm))

        htext ="<font size=15 name='boldFont'> Maintenance Schedule </font>"
        h = Paragraph(htext, normal)
        h.wrapOn(self.c, self.width, self.height)
        h.drawOn(self.c, *self.createCoordinate(0, 30 , mm))

    def createTable(self, datatext):
        pdfmetrics.registerFont(TTFont('boldFont', 'Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'Arial Bold.ttf'))

        styles = getSampleStyleSheet()
        stylesNormal = styles["Normal"]
        styleTitle = styles["Title"]

        # Header of Table 
        CH1 = Paragraph("<font size=10 name='boldFont'> TSID </font>", styleTitle)
        CH2 = Paragraph("<font size=10 name='boldFont'> Cust Name </font>", styleTitle)
        CH3 = Paragraph("<font size=10 name='boldFont'> Dept </font>", styleTitle)
        CH4 = Paragraph("<font size=10 name='boldFont'> Equip </font>", styleTitle)
        CH5 = Paragraph("<font size=10 name='boldFont'> Issue </font>", styleTitle)
        CH6 = Paragraph("<font size=10 name='boldFont'> SN </font>", styleTitle)
        CH7 = Paragraph("<font size=10 name='boldFont'> Tel </font>", styleTitle)
        CH8 = Paragraph("<font size=10 name='boldFont'> Status </font>", styleTitle)

        data = [
            ['page 1','','','','','','',''],
            [CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH8]
        ]

        # Data of Table

        textlist = datatext
        count = len(textlist)

        for i in range(count):
            t1 = Paragraph("<font size=9 name='boldFont'>{}</font>".format(textlist[i][0]), stylesNormal)
            t2 = Paragraph("<font size=9 name='boldFont'>{}</font>".format(textlist[i][1]), stylesNormal)
            t3 = Paragraph("<font size=9 name='boldFont'>{}</font>".format(textlist[i][2]), stylesNormal)
            t4 = Paragraph("<font size=9 name='boldFont'>{}</font>".format(textlist[i][3]), stylesNormal)
            t5 = Paragraph("<font size=9 name='boldFont'>{}</font>".format(textlist[i][4]), stylesNormal)
            t6 = Paragraph("<font size=9 name='boldFont'>{}</font>".format(textlist[i][5]), stylesNormal)
            t7 = Paragraph("<font size=9 name='boldFont'>{}</font>".format(textlist[i][6]), stylesNormal)
            t8 = Paragraph("<font size=9 name='boldFont'>{}</font>".format(textlist[i][7]), stylesNormal)
            data.append([t1, t2, t3, t4, t5, t6, t7, t8])

        # Table line full A4
        lineoftable = 35
        count2 = len(data)
        conntf = lineoftable - count2

        for i in range(conntf):
            data.append(['', '', '', '', '', '', '', ''])


        tableThatSplitsOverPages = Table(data,[2.5 * cm, 2.5 * cm, 2 * cm, 1.8 * cm, 
                                               4 * cm, 1.8 * cm, 2.2 * cm, 1.5 * cm], repeatRows=1)

        tableStyle = TableStyle(
            [ 
                ('BOX',(0,0),(-1,-1),1,colors.black),
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                ('FONTNAME', (0,0), (-1,-0), 'boldFont'),
                ('SPAN', (0,0), (-1,0)),
            ]
        )
        tableThatSplitsOverPages.setStyle(tableStyle)
        self.story.append(tableThatSplitsOverPages)

if __name__ == '__main__':
    pdffile ='GamePlan_Report.pdf'
    data = [
        ['12325253251', 'John Doe', 'IT', 'Laptop', 'Broken Screen', 'SN1234', '123456789', 'Open'],
        ['12325253252', 'Jane Doe', 'HR', 'Printer', 'Paper Jam', 'SN1235', '123456788', 'Open'],
        ['12325253253', 'John Smith', 'IT', 'Monitor', 'No Power', 'SN1236', '123456787', 'Open'],
        ['12325253254', 'Jane Smith', 'HR', 'Keyboard', 'Broken Key', 'SN1237', '123456786', 'Open'],
    ]
    Report_pdf().create_pdf(pdffile, data)
    subprocess.run(['open', pdffile])
        

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# Create a PDF document
doc = SimpleDocTemplate("example.pdf", pagesize=letter)

# Create a list to hold the content of the PDF
elements = []

# Define a style for the title
styles = getSampleStyleSheet()
title_style = styles["Title"]

# Create a title
title = Paragraph("Sample PDF Document", title_style)
elements.append(title)
elements.append(Spacer(1, 12))

# Create a table
data = [["Name", "Age"],
        ["John Doe", "30"],
        ["Jane Smith", "25"],
        ["Bob Johnson", "35"]]

table = Table(data)
table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                           ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

elements.append(table)

# Build the PDF document
doc.build(elements)

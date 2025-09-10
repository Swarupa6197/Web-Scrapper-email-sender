from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def generate_report(data, keyword="General"):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"report_{keyword}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join("reports", filename)

    c = canvas.Canvas(filepath, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 750, f"Web Scraping Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 730, f"Keyword: {keyword}")
    c.drawString(50, 710, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y = 680
    for i, item in enumerate(data, 1):
        if y < 50:  # new page
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750
        c.drawString(50, y, f"{i}. {item[:120]}")  # truncate
        y -= 20

    c.save()
    return filename

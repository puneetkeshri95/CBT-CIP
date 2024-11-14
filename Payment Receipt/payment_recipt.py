from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_receipt(from_address, to_address, payment_date, receipt_number, items, tax_rate):

    filename = f"receipt_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    

    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height - 50, "Payment Receipt")
    

    c.setFont("Helvetica", 12)
    c.drawString(width - 200, height - 80, f"Payment Date: {payment_date}")
    c.drawString(width - 200, height - 100, f"Receipt #: {receipt_number}")


    c.drawString(50, height - 120, "From:")
    y = height - 140
    for line in from_address:
        c.drawString(50, y, line)
        y -= 15


    c.drawString(300, height - 120, "Sold To:")
    y = height - 140
    for line in to_address:
        c.drawString(300, y, line)
        y -= 15
    

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Description")
    c.drawCentredString(275, y, "Quantity")
    c.drawCentredString(375, y, "Unit Price ($)")
    c.drawCentredString(475, y, "Total ($)")


    y -= 20
    subtotal = 0
    c.setFont("Helvetica", 12)
    for item in items:
        description, quantity, unit_price = item
        total = quantity * unit_price
        subtotal += total
        
    
        c.drawString(50, y, description) 
        c.drawCentredString(275, y, str(quantity)) 
        c.drawRightString(400, y, f"${unit_price:,.2f}") 
        c.drawRightString(500, y, f"${total:,.2f}") 
        
        y -= 20


    tax_amount = subtotal * (tax_rate / 100)
    total_amount = subtotal + tax_amount
    
    c.setFont("Helvetica-Bold", 12)
    c.drawRightString(400, y - 20, "Subtotal:")
    c.drawRightString(500, y - 20, f"${subtotal:,.2f}")
    
    c.drawRightString(400, y - 40, f"Tax (GST at {tax_rate}%):")
    c.drawRightString(500, y - 40, f"${tax_amount:,.2f}")
    
    c.drawRightString(400, y - 60, "Total Amount Due:")
    c.drawRightString(500, y - 60, f"${total_amount:,.2f}")
    

    c.setFont("Helvetica-Oblique", 10)
    footer_text = "Thank you for your purchase!\nFor inquiries, contact Global Health Pharmacy Ltd.\nCustomer service: +91 11 2345 6789."
    c.drawString(50, y - 100, footer_text)
    

    c.save()
    print(f"Receipt saved as {filename}")

def get_input():

    from_address = [
        "Global Health Pharmacy Ltd.",
        "123 Wellness Avenue,London",
        "+44 20 7946 0958",
        "GST No: GB123456789"
    ]


    to_address = [
        "Meow Singh",
        "456 Oak Street, Sydney, Australia",
        "+61 2 9876 5432"
    ]


    payment_date = "2024-11-06"
    receipt_number = "GH123456789"


    items = [
        ("Paracetamol 500mg Tablets", 1, 400.00),
        ("Ibuprofen 200mg Tablets", 2, 550.00),
        ("Cetirizine 10mg Tablets", 1, 300.00),
        ("Vitamin C 500mg Tablets", 2, 700.00),
        ("Antiseptic Cream 50g", 1, 450.00),
        ("Cough Syrup 100ml", 1, 600.00),
        ("Band-Aid", 1, 250.00),
        ("Digital Thermometer", 1, 1000.00),
        ("Hand Sanitizer 200ml", 2, 350.00),
        ("Eye Drops 15ml", 1, 400.00)
    ]


    tax_rate = 18.0


    generate_receipt(from_address, to_address, payment_date, receipt_number, items, tax_rate)


get_input()

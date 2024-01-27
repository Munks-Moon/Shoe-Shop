from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
import io

def payment_completed(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Shuswap Shoe Shop - Invoice no. {order.id}'
    message = 'Here is your invoice for your recent purchase'
    
    template = get_template('orders/pdf.html')
    context = {'order': order}
    html = template.render(context)

    pdf_file = io.BytesIO()
    pisa.CreatePDF(html, dest=pdf_file)
    
    email = EmailMessage(subject, message, 'admin@mystore.com', [order.email])
    email.attach(f'invoice_{order.id}.pdf', pdf_file.getvalue(), 'application/pdf')
    email.send()

    return HttpResponse('Invoice sent successfully')

    
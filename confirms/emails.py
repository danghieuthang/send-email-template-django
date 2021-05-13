from confirms.models import Order
from datetime import date
from asgiref.sync import sync_to_async
from templated_email import send_templated_mail
from core.emails import send_email
EMAIL_CHANGED_NOTIFICATION_TEMPLATE = "notifications/notification"
CONFIRM_ORDER_TEMPLATE = "order/confirm_order"

def send_notification_email():
    email = "dhthang1998@outlook.com"
    _send_user_change_email_notification(email)
    
def send_confirm_order(order: Order):
    _send_confirm_order(order)
  
def _send_confirm_order(order: Order):
    send_templated_mail(template_name=CONFIRM_ORDER_TEMPLATE,
        from_email='dhthang1998@gmail.com',
        recipient_list=[order.user_email],
        context=order.__dict__,
        headers={'My-Custom-Header':'Custom Value'})
    
def _send_user_change_email_notification(recipient_email):
    send_templated_mail(template_name=EMAIL_CHANGED_NOTIFICATION_TEMPLATE,
        from_email='dhthang1998@gmail.com',
        recipient_list=[recipient_email],
        context={
            'username':"This is my name",
            'full_name': "This is my fullname",
            'signup_date': date.today
        },
        headers={'My-Custom-Header':'Custom Value'})

def test_send(recipient_email) :
    _send_user_change_email_notification(recipient_email)
    
@sync_to_async
def test():
    for i in  range(1, 1000):
        pass
    

    
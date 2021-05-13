from confirms.models import Order
from datetime import date
from asgiref.sync import sync_to_async
from templated_email import send_templated_mail
from core.emails import send_email
EMAIL_CHANGED_NOTIFICATION_TEMPLATE = "notifications/notification"
CONFIRM_ORDER_TEMPLATE = "order/confirm_order"

def collect_data_for_email(
    order_pk: int, template: str, redirect_url: str = ""
) -> dict:
    """Collect the required data for sending emails."""
    order = Order.objects.prefetch_related("lines__variant__product__images").get(
        pk=order_pk
    )
    recipient_email = order.get_customer_email()
    send_kwargs, email_context = get_email_context()

    email_context["order_details_url"] = (
        prepare_order_details_url(order, redirect_url) if redirect_url else ""
    )
    email_context["order"] = order

    # Order confirmation template requires additional information
    if template in [CONFIRM_ORDER_TEMPLATE]:
        email_markup = get_order_confirmation_markup(order)
        email_context["schema_markup"] = email_markup

    return {
        "recipient_list": [recipient_email],
        "template_name": template,
        "context": email_context,
        **send_kwargs,
    }

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
        
@sync_to_async
def test():
    for i in  range(1, 1000):
        pass
    

    
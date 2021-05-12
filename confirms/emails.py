from templated_email import send_templated_mail
from urllib.parse import urlencode
from datetime import date
EMAIL_CHANGED_NOTIFICATION_TEMPLATE = "notifications/notification"

def send_notification_email():
    email = "dhthang1998@outlook.com"
    _send_user_change_email_notification(email)
    
def _send_user_change_email_notification(recipient_email):
    send_templated_mail(
        template_name=EMAIL_CHANGED_NOTIFICATION_TEMPLATE,
        from_email='dhthang1998@gmail.com',
        recipient_list=[recipient_email],
        context={
            'username':"This is my name",
            'full_name': "This is my fullname",
            'signup_date': date.today
        },
        # Optional:
        # cc=['cc@example.com'],
        # bcc=['bcc@example.com'],
        headers={'My-Custom-Header':'Custom Value'},
        # template_prefix="my_emails/",
        # template_suffix="email",
)
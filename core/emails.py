from templated_email import send_templated_mail

def send_email(template, recipients, context, header):
      send_templated_mail(
        template_name=template,
        from_email='dhthang1998@gmail.com',
        recipient_list=recipients,
        context=context,
        # cc=['cc@example.com'],
        # bcc=['bcc@example.com'],
        headers=header,
        # template_prefix="my_emails/",
        # template_suffix="email",
    )

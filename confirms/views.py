from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .emails import send_notification_email

@api_view(["POST"])
def sendTotification(request):
    send_notification_email()
    return Response(status=200)
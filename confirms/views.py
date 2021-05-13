from asyncio.tasks import Task
from confirms.models import Order
from core.utils import getVariables
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .emails import send_confirm_order, send_notification_email, test
import asyncio
import time

@api_view(["POST"])
def sendTotification(request):
    send_notification_email()
    return Response(status=200)

@api_view(["POST"])
def confimOrder(request):
    order = getVariables(request)
    orderU = Order(**order)
    send_confirm_order(orderU)
@api_view(["GET"])
async def asyncF(request):
    start = time.time()
    task1 = asyncio.ensure_future(test())
    task2 = asyncio.ensure_future(test())
    await asyncio.wait([task1, task2])
    print(time.time()-start)
    return Response(data="async", status=200)

@api_view(["GET"])
def syncF(request):
    start = time.time()
    test()
    test()
    print(time.time()-start)
    return Response(data="sync", status=200)
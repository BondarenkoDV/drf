# from django.http import HttpResponse
# from .tasks import my_first_task
#
#
# def index(request):
#     my_first_task.delay(6)
#     return HttpResponse('response completed!')
from rest_framework import generics
from .models import Tickets
from .serializers import TicketsSerializer


class TicketsAPIView(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class TicketAPIUpdate(generics.UpdateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

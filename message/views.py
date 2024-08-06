from django.views.generic import ListView #ListView komak mikone man data haro az database bekhonam
from .models import Message

class MessageView(ListView):
    model = Message #manzor inke biad az table database bekhone
    template_name = 'home.html'  # biad dakhel in on data haro neshon bede
    
from django.http import HttpResponseRedirect
from django.urls import reverse

from .rabbitmq_utils import send_message_to_rabbitmq


# Create your views here.
def send_message_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        tg_ids = request.POST.get('tg_ids')
        tg_ids = list(map(int, tg_ids.split(',')))
        # # Отправка сообщения в RabbitMQ
        send_message_to_rabbitmq(message, tg_ids)
        return HttpResponseRedirect(reverse('admin:shop_wd_user_changelist'))
    return HttpResponseRedirect(reverse('admin:index'))

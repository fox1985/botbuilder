
# bots/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import BotBlock


def block_list(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            BotBlock.objects.create(title="Новый блок", message="Новое сообщение")
        elif 'save_order' in request.POST:
            ids = request.POST.get('order', '').split(',')
            for i, block_id in enumerate(ids):
                BotBlock.objects.filter(id=block_id).update(position=i)
    blocks = BotBlock.objects.order_by('position')
    return render(request, 'bots/bot_blocks.html', {'blocks': blocks})


def export_json(request):
    data = list(BotBlock.objects.values())
    return JsonResponse(data, safe=False)

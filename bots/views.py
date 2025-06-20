
# bots/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BotBlock, BlockTransition
import json

def block_list(request):
    blocks = BotBlock.objects.all()
    return render(request, 'bots/bot_blocks.html', {'blocks': blocks})


@csrf_exempt
def save_diagram(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        blocks = data.get('blocks', [])
        connections = data.get('connections', [])

        # Очистим всё старое (опционально)
        BlockTransition.objects.all().delete()
        BotBlock.objects.all().delete()

        # Сохраняем блоки
        block_map = {}
        for block in blocks:
            obj = BotBlock.objects.create(
                id=int(block['id']),
                title=block['title'],
                message=block['message'],
                x=int(block['x']),
                y=int(block['y']),
                position=int(block['id'])
            )
            block_map[block['id']] = obj

        # Сохраняем связи
        for conn in connections:
            from_id = conn['source']
            to_id = conn['target']
            BlockTransition.objects.create(
                from_block=block_map[from_id],
                to_block=block_map[to_id],
                condition=conn.get('condition', '')
            )

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'invalid method'}, status=405)


def export_json(request):
    blocks = list(BotBlock.objects.values('id', 'title', 'message', 'x', 'y'))
    connections = list(BlockTransition.objects.values('from_block_id', 'to_block_id', 'condition'))
    return JsonResponse({'blocks': blocks, 'connections': connections})
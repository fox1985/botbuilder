
# bots/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BotBlock, BlockButton
import json


def block_list(request):
    blocks = BotBlock.objects.all()
    return render(request, 'bots/bot_blocks.html', {'blocks': blocks})


@csrf_exempt
def save_diagram(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        blocks = data.get('blocks', [])
        buttons = data.get('buttons', [])

        # Очистим старые данные
        BlockButton.objects.all().delete()
        BotBlock.objects.all().delete()

        # Сохраняем блоки
        block_map = {}
        for block in blocks:
            obj = BotBlock.objects.create(
                id=int(block['id']),
                title=block.get('title', f"Блок {block['id']}"),
                message=block.get('message', ''),
                block_type=block.get('type', 'message'),
                x=int(block.get('x', 0)),
                y=int(block.get('y', 0))
            )
            block_map[str(block['id'])] = obj

        # Сохраняем кнопки (переходы)
        for btn in buttons:
            block_id = str(btn.get('block_id'))
            to_block_id = str(btn.get('to_block_id'))
            BlockButton.objects.create(
                block=block_map.get(block_id),
                label=btn.get('label', ''),
                to_block=block_map.get(to_block_id)
            )

        return JsonResponse({'status': 'ok'})
    
    return JsonResponse({'error': 'invalid method'}, status=405)



def export_json(request):
    blocks = list(BotBlock.objects.values('id', 'title', 'message', 'x', 'y'))
    buttons = list(BlockButton.objects.values('block_id', 'label', 'to_block_id'))
    return JsonResponse({'blocks': blocks, 'buttons': buttons})


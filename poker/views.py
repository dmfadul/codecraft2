from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from .models import Position, RangeEntry
import json


class PositionCreateView(CreateView):
    model = Position
    fields = ['name']
    template_name = 'poker/position_form.html'
    success_url = reverse_lazy('add_position')

def poker_ranges(request):
    positions = Position.objects.all()
    hand_combinations = generate_hand_combinations()
    return render(request, "poker/poker_ranges.html", {"positions": positions, "hand_combinations": hand_combinations})

def save_range(request):
    if request.method == "POST":
        data = json.loads(request.body)
        position = Position.objects.get(id=data["position_id"])
        hand = data["hand"]
        action = data["action"]

        if action:
            RangeEntry.objects.update_or_create(position=position, hand=hand, defaults={"action": action})
        else:
            RangeEntry.objects.filter(position=position, hand=hand).delete()

        return JsonResponse({"status": "success"})
    
def generate_hand_combinations():
    ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    hands = [[f"{r1}{r2}s" if i < j else f"{r2}{r1}o" if i > j else f"{r1}{r2}" for i, r1 in enumerate(ranks)] for j, r2 in enumerate(ranks)]
    return hands

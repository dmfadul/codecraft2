from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from .models import Position, Context, StackDepth, RangeEntry
import json


class PositionCreateView(CreateView):
    model = Position
    fields = ['name', 'abbreviation', 'description', 'distance_from_button']
    template_name = 'poker/position_form.html'
    success_url = reverse_lazy('add_position')


class ContextCreateView(CreateView):
    model = Context
    fields = ['title', 'abbreviation', 'description']
    template_name = 'poker/context_form.html'
    success_url = reverse_lazy('add_context')


class StackDepthCreateView(CreateView):
    model = StackDepth
    fields = ['minimum', 'maximum']
    template_name = 'poker/stack_form.html'
    success_url = reverse_lazy('add_stackeX$')


def poker_ranges(request):
    positions = Position.objects.all()
    situations = Context.objects.all()
    stacks = StackDepth.objects.all()
    hand_combinations = generate_hand_combinations()
    return render(request, "poker/poker_ranges.html",
                  {"positions": positions,
                   "situations": situations,
                   "stacks": stacks,
                   "hand_combinations": hand_combinations})


def get_range(request, position):
    positions = Position.objects.all()
    selected_context = Context.objects.filter(abbreviation="RFI").first()
    selected_stack = StackDepth.objects.filter(minimum=50, maximum=100).first()
    position_obj = Position.objects.filter(abbreviation=position).first()

    hand_combinations_ = RangeEntry.objects.filter(position=position_obj,
                                                  context=selected_context,
                                                  stack_depth=selected_stack).all()
    
    if not hand_combinations_:
        hand_combinations_ = RangeEntry.gen_range(position_obj, selected_stack, selected_context)

    print(hand_combinations_)
    
    hand_combinations = generate_hand_combinations()
    return render(request, "poker/poker_ranges.html",
                  {"positions": positions,
                   "selected_position": position,
                   "hand_combinations": hand_combinations})


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
    hands = [[f"{r1}{r2}o" if i < j else f"{r2}{r1}s" if i > j else f"{r1}{r2}" for i, r1 in enumerate(ranks)] for j, r2 in enumerate(ranks)]
    return hands

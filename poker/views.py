from django.shortcuts import redirect, render
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
    # Check if query parameters exist
    position = request.GET.get("position", "UTG")
    context = request.GET.get("context", "RFI")
    stack_id = request.GET.get("stack_id", "1")  # Default to "1" but ensure it's an integer

    # Redirect to the get_range view with default values if they are not set
    return redirect("get_range", position=position, context=context, stack_id=int(stack_id))


def get_range(request, position, context, stack_id):
    positions = Position.objects.all()
    contexts = Context.objects.all()
    stacks = StackDepth.objects.all()


    position = Position.objects.filter(abbreviation=position).first()
    context = Context.objects.filter(abbreviation=context).first()
    stack = StackDepth.objects.filter(id=stack_id).first()

    hand_combinations = RangeEntry.load_range(position=position,
                                              context=context,
                                              stack_depth=stack)
    
    if not hand_combinations:
        hand_combinations = RangeEntry.gen_range(position, stack, context)

    return render(request, "poker/poker_ranges.html",
                  {"positions": positions,
                   "situations": contexts,
                   "stacks": stacks,
                   "selected_position": position.abbreviation,
                   "selected_situation": context.abbreviation,
                   "selected_stack_id": stack.id,
                   "hand_combinations": hand_combinations})


def save_range(request):
    if request.method == "POST":
        data = json.loads(request.body)
        hand = RangeEntry.objects.filter(id=data["hand"]).first()
        action = data["action"]

        if action:
            RangeEntry.objects.update_or_create(stack_depth=hand.stack_depth,
                                                context=hand.context,
                                                position=hand.position,
                                                hand=hand.hand,
                                                defaults={"action":action})

        return JsonResponse({"status": "success"})
    
def generate_hand_combinations():
    ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    hands = [[f"{r1}{r2}o" if i < j else f"{r2}{r1}s" if i > j else f"{r1}{r2}" for i, r1 in enumerate(ranks)] for j, r2 in enumerate(ranks)]
    return hands

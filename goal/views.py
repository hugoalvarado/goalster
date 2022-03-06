from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Goal

# Create your views here.
def goals(request):
    return render(request, 'goal/goals.html')

@require_http_methods(['POST'])
def add_todo(request):
    title = request.POST.get('title')

    if title:
        goal = Goal.objects.create(title=title)
        return render(request, 'goal/partials/goal.html', {'goal': goal})
    return render()

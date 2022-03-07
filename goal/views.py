from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Goal

# Create your views here.
def goals(request):
    goals = Goal.objects.all()
    return render(request, 'goal/goals.html', {'goals': goals})

@require_http_methods(['POST'])
def add_goal(request):
    title = request.POST.get('title')

    if title:
        goal = Goal.objects.create(title=title)
        return render(request, 'goal/partials/goal.html', {'goal': goal})
    return render(request, 'error.html')

from django.shortcuts import render

from .models import Profile, SkillCategory, Project, TimelineEntry


def home(request):
    context = {
        'profile': Profile.get_solo(),
        'skill_categories': SkillCategory.objects.prefetch_related('skills').all(),
        'projects': Project.objects.prefetch_related('tags').all(),
        'timeline': TimelineEntry.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)

from django.shortcuts import render


def resolve_resume(request):
    return render(request, 'resume/index.html', {})

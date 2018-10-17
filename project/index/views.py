from django.shortcuts import render


def index(request):
    """Return index(home) page."""
    return render(request, "index/index.html")

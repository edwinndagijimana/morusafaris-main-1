from django.shortcuts import render

from .models import footer, tour, team, service,htels


# Create your views here.
def index(request):
    footers = footer.objects.all()
    tours1 = tour.objects.all()[:2]
    teams = team.objects.all()
    tours = tour.objects.all()
    services = service.objects.all()

    context = {
        'services': services,
        'tours': tours,
        'tours1': tours1,
        'teams': teams,
        'footers': footers
    }

    return render(request, 'index.html', context)


def booking(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'bookings.html', context)


def about(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'about.html', context)


def amazing(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'amzingwild.html', context)


def contact_us(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'contact-us.html', context)


def hotels(request):
    footers = footer.objects.all()
    hotels = htels.objects.all()
    context = {
        'hotels': hotels,
        'footers': footers,
    }
    return render(request, 'hotels.html', context)


def safaris(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'safaris.html', context)


def tours(request):
    tours = tour.objects.all()
    footers = footer.objects.all()
    context = {
        'tours': tours,
        'footers': footers,
    }
    return render(request, 'typography.html', context)


def ultimateeastafrica(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'ultimateeastafrica.html', context)


def visitkenya(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'visitkenya.html', context)


def visitrwanda(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'visitrwanda.html', context)


def visittz(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'visittz.html', context)


def visituganda(request):
    footers = footer.objects.all()

    context = {
        'footers': footers,
    }
    return render(request, 'visituganda.html', context)


def blog(request):
    footers = footer.objects.all()
    context = {
        'footers': footers,
    }
    return render(request, 'blog.html', context)


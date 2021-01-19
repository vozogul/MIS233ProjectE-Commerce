from django.shortcuts import render, HttpResponse
from phoneapp.models import phoneSpecs


# Create your views here.
def index(request):
    return render(request, "base.html")


def phoneSearch(request):
    result_set = phoneSpecs.objects.filter


def search(request):
    errors = []
    if request.GET['q']:
        q = request.GET['q']
        print('query', q)
        if len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            phones = phoneSpecs.objects.filter(name__icontains=q)
            return render(request, 'searchresults.html', {'phones': phones, 'query': q})
    else:
        errors.append('Enter a search term.')

    return render(request, 'searchform.html', {'errors': errors})


def filter(request):
    errors = []
    if request.GET['minValue']:
        q = request.GET['minValue']
        print('query', q)
        if len(q) > 20:
            errors.append('Please enter proper characters.')
        else:
            phones=pricefilterMin(q)
            if request.GET['maxValue']:
                a = request.GET['maxValue']
                print('query', a)
                phoness=pricefilterMax(a,phones)
                return render(request, 'filterresults.html', {'phones': phoness, 'min': q, 'max':a})
    else:
        errors.append('Enter a search term.')

    return render(request, 'filterresults.html', {'errors': errors})


def pricefilterMin(q):
    k = int(q)
    j = 1000
    t = 1000

    for j in range(k):

        phonephone = phoneSpecs.objects.exclude(price__lt=j)

    return phonephone


def pricefilterMax(q, phones):
    k = int(q)
    j = 1000
    t = 1000

    for j in range(k):

        phonephone = phones.exclude(price__gt=k)

    return phonephone

def filterform(request):
    return render(request, 'filterform.html')


def searchform(request):
    return render(request, 'searchform.html')




def slidevalue(request):
    return render(request, HttpResponse("ghgg"))
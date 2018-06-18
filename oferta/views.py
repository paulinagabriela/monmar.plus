from django.shortcuts import render


def oferta_list(request):
        return render(request, 'oferta/oferta_list.html', {})


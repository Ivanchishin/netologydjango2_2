import os

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BASE_DIR


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    context = {
        #     'bus_stations': ...,
        #     'page': ...,
    }
    bus_list = []
    page_number = int(request.GET.get('page'))
    with open(os.path.join(BASE_DIR, 'data-398-2018-08-30.csv'), 'r+', encoding='utf-8') as file:
        content = csv.reader(file)
        for row in content:
            bus_st = {'Name': row[1], 'Street': row[4], 'District': row[6]}
            bus_list.append(bus_st)
    paginator = Paginator(bus_list, 20)
    page_obj = paginator.get_page(page_number)
    context['bus_stations'] = page_obj
    context['page'] = page_obj
    print(context)
    return render(request, 'stations/index.html', context)

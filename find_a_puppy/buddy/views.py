import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views import View

from buddy.models import RaceList


class IndexView(View):

    def get(self, request):
        return render(request, "index.html")


def RaceListView(request):
    b = RaceList.objects.all()
    paginator = Paginator(b, 2)
    page = request.GET.get('page')
    a = paginator.get_page(page)
    return render(request, "racelist.html", {'all_race': a})

#
# def RaceDetailsView(request, racelist_id):
#     race_details = []
#     race = RaceList.objects.all().filter(pk=racelist_id)
#     for value in race:
#         race_details.append({"name": value.name, 'description': value.description,
#                              'size': value.size, 'care': value.care, 'activity': value.activity,
#                              'children': value.children, 'character': value.character,
#                              'live_in_city': value.live_in_city, 'salary': value.salary,
#                              'training': value.training, 'save': value.save})
#         return render(request, "race-details.html", {'race_details': race_details})




import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View


from buddy.forms import FilterForm
from buddy.models import Race


class IndexView(View):

    def get(self, request):
        return render(request, "index.html")


def RaceListView(request):
    b = Race.objects.all()
    paginator = Paginator(b, 5)
    page = request.GET.get('page')
    a = paginator.get_page(page)
    return render(request, "racelist.html", {'all_race': a})


def RaceDetailsView(request, id):
    race_details = []
    race = Race.objects.all().filter(id=id)
    for value in race:
        race_details.append({"name": value.name, 'description': value.description,
                             'size': value.size, 'care': value.care, 'activity': value.activity,
                             'children': value.children, 'character': value.character,
                             'live_in_city': value.live_in_city, 'salary': value.salary,
                             'training': value.training, 'save': value.save})
        return render(request, "racedetail.html", {'race_details': race_details})


class RaceFilterView(View):
    def get(self, request):
        form = FilterForm()
        return render(request, 'find_puppy.html', {"form": form})

    def post(self, request):
        form = FilterForm(request.POST)
        races = Race.objects.filter(size=form["size"].value()).filter(care=form["care"].value()).filter\
            (activity=form["activity"].value()).filter(children=form["children"].value()).filter\
            (character=form["character"].value()).filter(live_in_city=form["live_in_city"].value()).filter\
            (salary=form["salary"].value()).filter(training=form["training"].value()).filter\
            (guard=form["guard"].value())
        # races2 = races.filter(care=form["care"].value())
        # if races:
        #     size =



        return render(request, 'find_puppy.html', {"form": form, "races": races})



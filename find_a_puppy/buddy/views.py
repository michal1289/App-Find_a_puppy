from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from buddy.forms import FilterForm
from buddy.models import Race, Contact


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
                             'size': value.get_size_display, 'care': value.get_care_display,
                             'activity': value.get_activity_display, 'children': value.get_children_display,
                             'character': value.get_character_display, 'live_in_city': value.get_live_in_city_display,
                             'salary': value.get_salary_display, 'training': value.get_training_display,
                             'save': value.get_guard_display})
        return render(request, "racedetail.html", {'race_details': race_details})


class RaceFilterView(View):
    def get(self, request):
        form = FilterForm()
        return render(request, 'find_puppy.html', {"form": form})

    def post(self, request):
        form = FilterForm(request.POST)
        races = Race.objects.all()

        race_size = form["size"].value()
        race_care = form["care"].value()
        race_activity = form["activity"].value()
        race_children = form["children"].value()
        race_character = form["character"].value()
        race_live_in_city = form["live_in_city"].value()
        race_salary = form["salary"].value()
        race_training = form["training"].value()
        race_guard = form["guard"].value()

        if not race_size == "1":
            races = races.filter(size=race_size)
        if race_care != "1":
            races = races.filter(care=race_care)
        if race_activity != "1":
            races = races.filter(activity=race_activity)
        if race_children != "1":
            races = races.filter(children=race_children)
        if race_character != "1":
            races = races.filter(character=race_character)
        if race_live_in_city != "1":
            races = races.filter(live_in_city=race_live_in_city)
        if race_salary != "1":
            races = races.filter(salary=race_salary)
        if race_training != "1":
            races = races.filter(training=race_training)
        if race_guard != "1":
            races = races.filter(guard=race_guard)

        return render(request, 'find_puppy.html', {"form": form, "races": races})


class ContactView(CreateView):
    model = Contact
    fields = "__all__"
    success_url = ("/")

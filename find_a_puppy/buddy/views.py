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
        races = Race.objects.filter(size=form["size"].value()).filter(care=form["care"].value()).filter\
            (activity=form["activity"].value()).filter(children=form["children"].value()).filter\
            (character=form["character"].value()).filter(live_in_city=form["live_in_city"].value()).filter\
            (salary=form["salary"].value()).filter(training=form["training"].value()).filter\
            (guard=form["guard"].value())
        # if races:

        return render(request, 'find_puppy.html', {"form": form, "races": races})


def FarmList(request):
    pass

from django import forms
from buddy.models import SIZE, CARE, ACTIVITY, CHILDREN, CHARACTER, LIVE_IN_CITY, SALARY, TRAINING, GUARD


class FilterForm(forms.Form):
    size = forms.ChoiceField(label="Wielkość psa", choices=SIZE)
    care = forms.ChoiceField(label="Pielęgnacia sierści", choices=CARE)
    activity = forms.ChoiceField(label="Aktywność fizyczna psa", choices=ACTIVITY)
    children = forms.ChoiceField(label="Pies a dziecko", choices=CHILDREN)
    character = forms.ChoiceField(label="Charakter", choices=CHARACTER)
    live_in_city = forms.ChoiceField(label="Mieszkanie w mieście", choices=LIVE_IN_CITY)
    salary = forms.ChoiceField(label="Koszty utrzyania", choices=SALARY)
    training = forms.ChoiceField(label="Szkolenie", choices=TRAINING)
    guard = forms.ChoiceField(label="Czy nadaje się jako stróż", choices=GUARD)

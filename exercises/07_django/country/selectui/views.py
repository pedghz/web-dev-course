from django.shortcuts import render, get_object_or_404

from countrydata.models import Continent
from countrydata.models import Country


def show_continent(request, continent_code=None):
    context = {
        "all_continents": Continent.objects.all()
    }
    if continent_code:
        continent = get_object_or_404(Continent, code=continent_code)
        context["continent"] = continent
        if continent:
            countries = Country.objects.filter(continent__code=continent_code)
            context["countries"] = countries
    if request.is_ajax():
        return render(request, "selectui/countrytable.html", context)

    # Add your answer in 7.3 here
    return render(request, "selectui/index.html", context)

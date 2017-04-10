from django.http import HttpResponse, Http404
import json


from countrydata.models import Continent, Country


def continent_json(request, continent_code):
    try:
        countries = Country.objects.filter(continent__code=continent_code)
        response_data = {}
        for country in countries:
            response_data[country.code] = country.name
        json_string = json.dumps(response_data)
        if 'callback' in request.GET:
            json_string = '%s(%s);' % (request.GET['callback'], json_string)
            return HttpResponse(json_string, "text/javascript")
        return HttpResponse(json_string, content_type="application/json")
    except:
        raise Http404("Not implemented")


def country_json(request, continent_code, country_code):
    try:
        country = Country.objects.filter(continent__code=continent_code).get(code = country_code)
        response_data = {}
        response_data['area'] = country.area
        response_data['population'] = country.population
        response_data['capital'] = country.capital
        json_string = json.dumps(response_data)
        if 'callback' in request.GET:
            json_string = '%s(%s);' % (request.GET['callback'], json_string)
            return HttpResponse(json_string, "text/javascript")
        return HttpResponse(json_string, content_type="application/json")
    except:
        raise Http404("Not implemented")

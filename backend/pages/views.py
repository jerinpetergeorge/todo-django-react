import requests
from django.http import JsonResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


def user_list(request):
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url=url)
    return JsonResponse(data=response.json(), safe=False)

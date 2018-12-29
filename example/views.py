
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class HomePageView(TemplateView):
    @csrf_exempt
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


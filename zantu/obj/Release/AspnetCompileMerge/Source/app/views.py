"""
Definition of views.
"""

#from django.shortcuts import render
#from django.http import HttpRequest
#from django.template import RequestContext
#from datetime import datetime

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import ListView, DetailView
from os import path

import json
from app.models import Tourguide


class TourGuideListView(ListView):
    """Renders the home page, with a list of all polls."""
    model = Tourguide

    def get_context_data(self, **kwargs):
        context = super(TourGuideListView, self).get_context_data(**kwargs)
        context['title'] = 'Tour Guides'
        context['year'] = datetime.now().year
        return context

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def seed(request):
    """Seeds the database with sample polls."""
    samples_path = path.join(path.dirname(__file__), 'samples.json')
    with open(samples_path, 'r') as samples_file:
        samples_polls = json.load(samples_file)

    for sample_poll in samples_polls:
        tg = Tourguide()
        tg.name  = sample_poll['name']
        tg.gender  = sample_poll['gender']
        tg.yearsOfExperience  = sample_poll['yearsOfExperience']
        poll.pub_date = timezone.now()
        poll.save()

    return HttpResponseRedirect(reverse('app:home'))

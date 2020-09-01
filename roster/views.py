from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

list = [
    { 
    'name':'Jack Xie',
    'event':'Fl/IM', 
    'group':'XX'
    },
    {
    'name':'Iris wang',
    'event':'Fr', 
    'group':'XX'
    }

]


def rosterView(request):
    context = {'list' : list, 'group':list[0].get('group')}
    return render(request, 'roster.html', context)


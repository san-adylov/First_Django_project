from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'my_members': mymembers
    }
    return HttpResponse(template.render(context, request))


def details(reqest, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_member': mymember
    }
    return HttpResponse(template.render(context, reqest))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))

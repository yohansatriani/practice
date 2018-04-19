from django.template.loader import get_template, render_to_string
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from practice.forms import ContactForm
import datetime
import MySQLdb

def hello(request):
    return HttpResponse("Hello World")

def boot(request):
    html = render_to_string('boot.html', {'title': "BOOTSTRAP-DJANGO-MANUAL", 'head': "Bootstrap 4.0 on Django 2.0"})
    return HttpResponse(html)

def main(request):
    html = render_to_string('main.html', {'title': "BOOTSTRAP-DJANGO", 'head': "create main html with include script"})
    return HttpResponse(html)

def current_datetime(request) :
    now = datetime.datetime.now()
    html = "<html><head><title>Time</title></head><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def present_time(request) :
    now = datetime.datetime.now()
    t = Template("<html><head><title>Time</title></head><body>It is now {{ thistime }}.</body></html>")
    html = t.render(Context({ 'thistime': now }))
    return HttpResponse(html)

def open_time(request) :
    now = datetime.datetime.now()
    fp = open('/venv/web/practice/templates/current_datetime.html')
    t = Template(fp.read())
    fp.close()

    html = t.render(Context({ 'current_date': now }))
    return HttpResponse(html)

def right_time(request) :
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({ 'current_date': now })
    return HttpResponse(html)

def in_time(request) :
    now = datetime.datetime.now()
    html = render_to_string('current_datetime.html', {'current_date': now})
    return HttpResponse(html)

def short_time(request) :
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><head><title>Page Title</title></head><body>In %s hour(s), it will be %s</body></html>" % (offset, dt)
    return HttpResponse(html)

def login(request):
    html = render_to_string('login.html', {'title': "Login", 'head': "Login"})
    return HttpResponse(html)

def film_list(request):
    db = MySQLdb.connect(user='mydba', db='sakila', passwd='mydba', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT title FROM film ORDER BY title ASC')
    film = [row[0] for row in cursor.fetchall()]
    db.close()
    return render(request, 'film_list.html', {'film': film})

def request_data(request):
    try:
        ro = [
            request.path,
            request.get_host(),
            request.get_full_path(),
            request.is_secure(),
            request.META['HTTP_USER_AGENT'],
            ]
    except KeyError:
        ro = ['unknown']
    return render(request, 'reqobject.html', {'title': "Django Request", 'head': "Requested Object Data", 'object': ro})

def meta_data(request):
    rm = request.META.items()
    
    return render(request, 'metaobject.html', {'title': "Django Request Meta", 'head': "Requested Meta Data Object", 'object': rm})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', ['noreply@example.com'] ("mailto:'noreply%40example.com")),
                [['siteowner@example.com']("mailto:'siteowner%40example.com")],
                )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})

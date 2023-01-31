from datetime import datetime

from django.shortcuts import render, redirect

from tasks.celery import debug_task
from travel_site import settings
from .forms import SignInForm, SignUpForm, ImageForm, MessageForm
from passlib.hash import pbkdf2_sha256
from django.views import generic

from .helper import is_auth
from .models import Person, Message, News, Air_ticket, Hotel, Food, Car, Place_to_go

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if len(Person.objects.filter(email=form.data.get("email"))) == 1:
            password = Person.objects.filter(email=form.data.get("email")).get().password
            if pbkdf2_sha256.verify(form.data.get("password"),password):
                request.session['email'] = form.data.get("email")
                return redirect("/users/main")
            else:
                return render(request, 'sign_in.html',{"form":SignInForm(),'message': 'Не правильный логин или пароль'})
        else:
            return render(request, 'sign_in.html',{"form":SignInForm(),'message': 'Пользователь не существует'})
    form =  SignInForm()
    return render(request,'sign_in.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if len(Person.objects.filter(email = form.data.get('email'))) != 0:
            return render(request, 'sign_up.html',{"form": SignUpForm(),'message': 'Пользователь уже существует'})
        password = SignUpForm(request.POST).data.get("password")
        Person(email=form.data.get("email"),name=form.data.get("name") ,password=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)).save()

        debug_task.apply_async(args=[form.data.get('email')])

        return redirect('/users/signin')
    form = SignUpForm()
    return render(request,'sign_up.html',{'form': form,})

@is_auth
def profile(request):
    if request.method == 'POST':
        person = Person.objects.get(email=request.session["email"])
        file_name = request.FILES['picture']
        full_path = str(settings.MEDIA_ROOT)+"/"+str(file_name)
        with open(full_path, 'wb+') as destination:
            for chunk in file_name.chunks():
                destination.write(chunk)
        Person.objects.update_or_create(email=person.email,defaults={'picture': settings.MEDIA_URL+str(file_name)})

    message = {"form": ImageForm(),"message": Person.objects.get(email=request.session["email"]).name,"image":Person.objects.get(email=request.session["email"]).picture}
    return render(request, 'profile.html',message)

# @login_required(login_url='/users/signin')
@is_auth
def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        Message(user_id=Person.objects.get(email=request.session["email"]),text=form.data.get('text'),date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')).save()

    qs = []
    for i in Message.objects.order_by('date'):
        if request.session["email"] == i.user_id.email:
            i.isOwner = True
        qs.append(i)
    qs.reverse()

    message = {"form": MessageForm(),"messages": qs}
    return render(request, 'message.html', message)


class MainPageView(generic.TemplateView):
    template_name = 'main_page.html'


class NewsView(generic.ListView):
    template_name = 'news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.order_by('date')


class AirTicketsView(generic.ListView):
    template_name = 'air_tickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return Air_ticket.objects.filter()


class HotelsView(generic.ListView):
    template_name = 'hotels.html'
    context_object_name = 'hotels'

    def get_queryset(self):
        return Hotel.objects.filter()


class RestaurantsView(generic.ListView):
    template_name = 'restaurants.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return Food.objects.filter()


class CarsView(generic.ListView):
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter()


class AttractionsView(generic.ListView):
    template_name = 'attractions.html'
    context_object_name = 'attractions'

    def get_queryset(self):
        return Place_to_go.objects.filter()


def exit(request):
    if len(request.session.keys()) > 0:
        del request.session['email']
    return redirect("/users/signin")




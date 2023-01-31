from django.db.models import Q, Sum, F
from django.shortcuts import render
from django.views import View

from myadmin.forms import TablesForm, CarNameForm, CarPriceForm, AddTicketForm
from users.helper import is_admin
from users.models import Person, Air_ticket, News, Message, Place_to_go, Hotel, Food, Car


def get_user(request,id):
    print(id)
    if len(Person.objects.filter(id=id)) == 1:
        person = Person.objects.filter(id=id).get()
        if person.picture == None:
            person.picture = "null"
        message = {"user": person}
    else:
        message = {"user": "Not Found"}
    print(message)
    return render(request, 'admin.html', message)

class GetTables(View):
    @is_admin
    def get(self,request):
        return render(request, 'tables.html')
    def post(self,request):
        form = TablesForm(request.POST)
        if form.is_valid():
            if form.data.get("table") == "Users":
                message = {"result": Person.objects.filter(),"tab":"Users"}
            if form.data.get("table") == "Air tickets":
                message = {"result": Air_ticket.objects.filter(),"tab":"Air tickets"}
            if form.data.get("table") == "News":
                message = {"result": News.objects.filter(),"tab":"News"}
            if form.data.get("table") == "Messages":
                message = {"result": Message.objects.filter(),"tab":"Messages"}
            if form.data.get("table") == "Attractions":
                message = {"result": Place_to_go.objects.filter(),"tab":"Attractions"}
            if form.data.get("table") == "Hotels":
                message = {"result": Hotel.objects.filter(),"tab":"Hotels"}
            if form.data.get("table") == "Restaurants":
                message = {"result": Food.objects.filter(),"tab":"Restaurants"}
            if form.data.get("table") == "Cars":
                print(Car.objects.aggregate(Sum(F('price')))) # class F
                message = {"result": Car.objects.filter(),"tab":"Cars"}
            if form.data.get("table") == "sortUsers":
                message = {"result": Person.objects.order_by('id'),"tab":"Users"}
            if form.data.get("table") == "sortTickets":
                message = {"result": Air_ticket.objects.order_by('price'),"tab":"Air tickets"}
        if not form.is_valid():
            form = CarNameForm(request.POST)
            form1 = CarPriceForm(request.POST)
            if form.is_valid() & form1.is_valid():
                message = {"result": Car.objects.filter(Q(name__icontains=form.data.get("name")) & Q(price__lte=form.data.get("price"))), "tab": "Cars"}
            if form.is_valid() &  (not form1.is_valid()):
                message = {"result": Car.objects.filter(name__icontains=form.data.get("name")), "tab": "Cars"}
            if (not form.is_valid()) & form1.is_valid():
                message = {"result": Car.objects.filter(price__lte=form.data.get("price")), "tab": "Cars"}
            if (not form.is_valid()) & (not form1.is_valid()):
                message = {"result": Car.objects.filter(), "tab": "Cars"}
        return render(request, 'tables.html', message)

class AddTickets(View):
    @is_admin
    def get(self,request):
        form = AddTicketForm()
        return render(request, 'add_ticket.html',{"form":form})
    def post(self,request):
        form = AddTicketForm(request.POST)
        if form.is_valid():
            form.save()
            message = {"message":"Добавлено","form":AddTicketForm()}
            return render(request, 'add_ticket.html', message)
        else:
            message = {"message": "Ошибка", "form": AddTicketForm()}
            return render(request, 'add_ticket.html', message)





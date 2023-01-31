from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255,default=None,verbose_name="name")
    email = models.CharField(max_length=255)
    picture = models.TextField(max_length=500 ,null=True ,default=None)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=100,default='USER')

    def __str__(self):
        return "Person{name = "+self.name+",email = "+ self.email+",picture = "+self.picture+",password = "+self.password+",role = "+self.role+"}"

class Message(models.Model):
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE,verbose_name="user")
    text = models.TextField(max_length=500)
    date = models.DateTimeField(default=None)
    isOwner = models.BooleanField(default=False)

class Air_ticket(models.Model):
    departure_place = models.CharField(max_length=255)
    arrival_place = models.CharField(max_length=255)
    date = models.DateTimeField()
    price = models.IntegerField()
    air_company = models.CharField(max_length=100,default=None)

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.IntegerField(default=None)
    text = models.TextField(max_length=500,default=None)

class Food(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    text = models.TextField(max_length=500,default=None)

class Car(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.IntegerField(default=None)
    text = models.TextField(max_length=500,default=None)

class Place_to_go(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=1000, default=None)
    address = models.CharField(max_length=255)
    price = models.IntegerField()

class News(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(default=None)

# class Favorites(models.Model):
#     id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     id_place_to_go = models.ForeignKey(Place_to_go, on_delete=models.CASCADE)
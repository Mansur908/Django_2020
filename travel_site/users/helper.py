from django.shortcuts import redirect

from users.models import Person


def is_auth(func):
    def wrapper(*args,**kwargs):
        if len(args[0].session.keys()) == 0:
            result = redirect("/users/signin")
        else:
            result = func(*args,**kwargs)
        return result
    return wrapper

def is_admin(func):
    def wrapper(*args,**kwargs):
        print()
        print(args)
        print()
        if len(args[1].session.keys()) == 0:
                result = redirect("/users/signin")
        else:
            person = Person.objects.get(email=args[1].session["email"])
            if person.role == "ADMIN":
                result = func(*args, **kwargs)
            else:
                result = redirect("/users/main")
        return result
    return wrapper
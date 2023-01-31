from django.core.management import BaseCommand

from users.models import Person


class Command(BaseCommand):
    help = "Number of registered users"

    def handle(self, *args, **options):
        users = Person.objects.filter()
        print(users.count())
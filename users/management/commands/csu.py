from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin',
            fio='admin',
            phone='+71111111111',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        user.set_password('111')
        user.save()

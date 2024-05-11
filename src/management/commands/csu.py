from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Automatically creates a superuser'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', None, 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created successfully\n'
                                                 'Login: admin\n'
                                                 'Password: admin123\n'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))

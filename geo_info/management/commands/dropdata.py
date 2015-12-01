from django.utils import timezone
from datetime import timedelta
from django.core.management.base import BaseCommand
from geo_info.models import GeoInfo


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('date', nargs='?', type=int, default=3)

    def handle(self, *args, **options):
        date = timezone.now()-timedelta(days=options['date'])
        GeoInfo.objects.filter(date__lte=date).delete()

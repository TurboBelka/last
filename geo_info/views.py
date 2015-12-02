from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from geoip2 import database
from geo_info.models import GeoInfo
from datetime import timedelta


def country_by_ip(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    # ip = '80.254.2.190'
    path = '%s/%s' % (settings.BASE_DIR, 'GeoLite2-Country.mmdb')
    reader = database.Reader(path)
    try:
        country = reader.country(ip).country.name
        headers = {k:v for k,v in request.META.iteritems() if k.startswith('HTTP')}
        user_agent = headers.get('HTTP_USER_AGENT')
        date_request = timezone.now()

        GeoInfo.objects.create(ip=ip, country=country, user_agent=user_agent,
                               headers=headers, date=date_request)
    except:
        pass
    return HttpResponse()


class GeoInfoView(generic.ListView):
    model = GeoInfo
    template_name = 'geo_info.html'
    context_object_name = 'geo_info'

    def get_queryset(self):
        date = timezone.now()-timedelta(days=3)
        return self.model.objects.filter(date__gte=date)


def delete_data(request):
    if request.method == 'POST':
        count_days = request.POST.get('days')
        if count_days:
            days = timezone.now()-timedelta(days=int(count_days))
            GeoInfo.objects.filter(date__lte=days).delete()
    return HttpResponseRedirect(reverse_lazy('geo_info:geo_info'))

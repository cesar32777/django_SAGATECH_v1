from django.conf import settings

def root_url(request):
    """
    Pass your root_url from the settings.py
    """
    return {'sagatech.com.mx': settings.ROOT_URL_YOU_WANT_TO_MENTION}
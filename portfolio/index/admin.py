from django.contrib import admin

from .models import about
from .models import slider
from .models import client
from .models import location
from .models import external_contact

admin.site.register(about)
admin.site.register(slider)
admin.site.register(client)
admin.site.register(location)
admin.site.register(external_contact)
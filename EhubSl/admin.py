from django.contrib import admin
from .models import message
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User

class MyAdminSite(AdminSite):
    site_title = gettext_lazy('Ehub admin')

    site_header = gettext_lazy('E-Hub super administration')

    index_title = gettext_lazy('Site administration')

admin_site = MyAdminSite()
# Register your models here.
admin.site.register(message)
admin_site.register(message)
admin_site.register(User)
from django.contrib import admin

from .models import Hududlar, Vaqt

admin.site.register(Hududlar)
admin.site.register(Vaqt)

admin.sites.AdminSite.site_title = "Jasurbek"
admin.sites.AdminSite.index_title = "Ramazon Taqvimi 2023"
admin.sites.AdminSite.site_header = "Ramazon Taqvimi 2023"
admin.sites.AdminSite.site_url = "/api"

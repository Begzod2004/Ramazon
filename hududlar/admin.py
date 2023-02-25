from django.contrib import admin

from .models import *

admin.site.register(Hududlar)
admin.site.register(Vaqt)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Video)
admin.site.register(VideoCategory)
admin.site.register(Viloyat)
admin.site.register(NamozVaqti)

admin.sites.AdminSite.site_title = "Taqvim"
admin.sites.AdminSite.index_title = "Ramazon Taqvimi 2023"
admin.sites.AdminSite.site_header = "Ramazon Taqvimi 2023"
admin.sites.AdminSite.site_url = "/api"

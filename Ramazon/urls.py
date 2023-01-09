from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def hello(request):
    html = "<html><body>Hello, This is landing page</body></html>"
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("hududlar.urls")),
    path("", hello)
]

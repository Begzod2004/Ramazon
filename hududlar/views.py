from datetime import time

from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from hududlar.models import Hududlar, Vaqt
from hududlar.serializers import HududSerializer, VaqtSerializer


class CreateHudud(CreateAPIView):
    name = "Hududlar"
    serializer_class = HududSerializer


class CreateVaqt(CreateAPIView):
    name = "Vaqtlar"
    serializer_class = VaqtSerializer


class HududlarView(APIView):
    def get(self, request):
        queryset = Hududlar.objects.all().values()
        return JsonResponse({"data:": list(queryset)})


class HududlarVaqt(APIView):
    def post(self, request):
        hudud = request.POST["hudud_id"]
        queryset = Vaqt.objects.filter(hudud=hudud).order_by("sana").values()
        data = list(queryset)
        for i in data:
            i["hudud"] = Hududlar.objects.get(id=hudud).nomi
            i.pop("id")
        return JsonResponse({"data:": data})


class AutoCreateHudud(APIView):

    @staticmethod
    def solve(vaqt, farq):
        soat = vaqt.hour
        minut = vaqt.minute + farq
        if minut >= 60:
            minut = minut - 60
            soat = soat + 1
            if soat == 24:
                soat = 0
        if minut < 0:
            minut = minut + 60
            soat = soat - 1
            if soat == -1:
                soat = 23
        return time(hour=soat, minute=minut)

    def post(self, request):
        try:
            hudud_nomi = request.POST["hudud_nomi"]
            vaqt_farqi = request.POST["vaqt_farqi"]
            hudud = Hududlar.objects.create(nomi=hudud_nomi, vaqt_farqi=vaqt_farqi)
            queryset = list(Vaqt.objects.filter(hudud=1).values())
            vaqt_farqi = int(vaqt_farqi)
            for i in queryset:
                Vaqt.objects.create(
                    sana=i["sana"],
                    ochish=self.solve(i["ochish"], vaqt_farqi),
                    yopish=self.solve(i["yopish"], vaqt_farqi),
                    hudud_id=hudud.id
                )
            return JsonResponse({})
        except Exception as e:
            return JsonResponse(status=400, data={"message": str(e)})

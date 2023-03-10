from datetime import time

from django.http import JsonResponse
from rest_framework.generics import CreateAPIView , RetrieveAPIView
from rest_framework.views import APIView

from hududlar.models import *
from hududlar.serializers import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import FormParser, MultiPartParser


class HududRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Hududlar.objects.all()
    serializer_class = HududSerializer
    parser_classes = (FormParser, MultiPartParser)


class HududList(generics.ListCreateAPIView):
    queryset = Hududlar.objects.all()
    serializer_class = HududSerializer
    # permission_classes = [IsAdminUser]
    parser_classes = (FormParser, MultiPartParser)


class VaqtRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Vaqt.objects.all()
    serializer_class = VaqtSerializer
    parser_classes = (FormParser, MultiPartParser)


class VaqtList(generics.ListCreateAPIView):
    queryset = Vaqt.objects.all()
    serializer_class = VaqtSerializer
    # permission_classes = [IsAdminUser]
    parser_classes = (FormParser, MultiPartParser)



class CreateHudud(CreateAPIView):
    name = "Hududlar"
    queryset = Hududlar.objects.all()
    serializer_class = HududSerializer
    parser_classes = (FormParser, MultiPartParser)


class CreateVaqt(CreateAPIView):
    name = "Vaqtlar"
    queryset = Vaqt.objects.all() #qoshdim bilmagan edim nimaga yoq ekanligini
    serializer_class = VaqtSerializer
    parser_classes = (FormParser, MultiPartParser)
    


class HududlarView(APIView):
    def get(self, request):
        queryset = Hududlar.objects.all().values()
        return JsonResponse({"data:": list(queryset)})


class HududlarVaqt(APIView):
    def post(self, request):
        try:
            hudud = request.POST["hudud_id"]
            queryset = Vaqt.objects.filter(hudud=hudud).order_by("sana").values()
            data = list(queryset)
            for i in data:
                i["hudud"] = Hududlar.objects.get(hudud_id=hudud).nomi
                i.pop("hudud_id")
            return JsonResponse({"data:": data})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)



# class HududlarVaqt(APIView):
#     def post(self, request):
#         hudud_id = request.data.get("hudud_id")
#         if hudud_id is None:
#             return JsonResponse({"error": "Missing 'hudud_id' key in request data"}, status=400)
        
#         queryset = Vaqt.objects.filter(hudud=hudud_id).order_by("sana").values()
#         data = list(queryset)
#         for i in data:
#             i["hudud"] = Hududlar.objects.get(id=hudud_id).nomi
#             i.pop("id")
#         return JsonResponse({"data:": data})



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
        

class AutoCreateViloyat(APIView):
    @staticmethod
    def creator(vaqt, farq):
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
            viloyat_nomi = request.POST["viloyat_nomi"]
            vaqt_farqi = request.POST["vaqt_farqi"]
            viloyat = Viloyat.objects.create(nomi=viloyat_nomi, vaqt_farqi=vaqt_farqi)
            queryset = list(NamozVaqti.objects.filter(viloyat=1).values())
            vaqt_farqi = int(vaqt_farqi)
            for i in queryset:
                NamozVaqti.objects.create(
                    sana=i["sana"],
                    bomdod=self.creator(i["bomdod"], vaqt_farqi),
                    peshin=self.creator(i["peshin"], vaqt_farqi),
                    asr=self.creator(i["asr"], vaqt_farqi),
                    shom=self.creator(i["shom"], vaqt_farqi),
                    xufton=self.creator(i["xufton"], vaqt_farqi),
                    viloyat_id=viloyat.id
                )
            return JsonResponse({})
        except Exception as b:
            return JsonResponse(status=400, data={"message": str(b)})
        



class ViloyatRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Viloyat.objects.all()
    serializer_class = ViloyatSerializer
    parser_classes = (FormParser, MultiPartParser)


class ViloyatList(generics.ListCreateAPIView):
    queryset = Viloyat.objects.all()
    serializer_class = ViloyatSerializer
    permission_classes = [IsAdminUser]
    parser_classes = (FormParser, MultiPartParser)




class NamozVaqtiRetrieveAPIView(generics.RetrieveAPIView):
    queryset = NamozVaqti.objects.all()
    serializer_class = NamozVaqtiSerializer
    parser_classes = (FormParser, MultiPartParser)


class NamozVaqtiList(generics.ListCreateAPIView):
    queryset = NamozVaqti.objects.all()
    serializer_class = NamozVaqtiSerializer
    # permission_classes = [IsAdminUser]
    parser_classes = (FormParser, MultiPartParser)



class CreateViloyat(CreateAPIView):
    name = "Viloyat"
    queryset = Viloyat.objects.all()
    serializer_class = ViloyatSerializer
    parser_classes = (FormParser, MultiPartParser)


class CreateNamozVaqti(CreateAPIView):
    name = "NamozVaqtilar"
    queryset = NamozVaqti.objects.all() #qoshdim bilmagan edim nimaga yoq ekanligini
    serializer_class = NamozVaqtiSerializer
    parser_classes = (FormParser, MultiPartParser)
    


class ViloyatView(APIView):
    def get(self, request):
        queryset = Viloyat.objects.all().values()
        return JsonResponse({"data:": list(queryset)})


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class VideoCategoryList(generics.ListAPIView):
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer



class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class HududUpdate(APIView):
    
    @staticmethod
    def hudud_updater():
        # try:
            Hududlar.objects.filter(nomi="Toshkent").update(hudud_id=1)
            Hududlar.objects.filter(nomi="Andijon").update(hudud_id=2)
            Hududlar.objects.filter(nomi="Namangan").update(hudud_id=3)
            Hududlar.objects.filter(nomi="Qo'qon").update(hudud_id=4)
            Hududlar.objects.filter(nomi="Guliston").update(hudud_id=5)
            Hududlar.objects.filter(nomi="Jizzax").update(hudud_id=6)
            Hududlar.objects.filter(nomi="Termiz").update(hudud_id=7)
            Hududlar.objects.filter(nomi="Samarqand").update(hudud_id=8)
            Hududlar.objects.filter(nomi="Buxoro").update(hudud_id=9)
            Hududlar.objects.filter(nomi="Navoiy").update(hudud_id=10)
            Hududlar.objects.filter(nomi="Urganch").update(hudud_id=11)
            Hududlar.objects.filter(nomi="Nukus").update(hudud_id=12)
            Hududlar.objects.filter(nomi="Qarshi").update(hudud_id=13)
            return True
        # except:
        #     return False

    def get(self, request):
        if self.hudud_updater():
            return JsonResponse({"data":"success"})
        else:
            return JsonResponse({}, status=400)





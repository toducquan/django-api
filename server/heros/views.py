from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hero as HeroModel
from .serializers import HeroSerializer

hero_added = []

# Create your views here.

def Index(requets):
    return render(request= requets, template_name='index.html', context={'text': 'hello world'})

class AllHeros(APIView):
    def get(self, request):
        heros = HeroModel.objects.all()
        serializer = HeroSerializer(heros, many = True)
        return Response(data=serializer.data, status= 200)
    def post(self, request):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            hero = serializer.save()
            hero_added.append(serializer.data)
            print(hero_added)
            return Response(data={"mess": "add successfully"}, status=200)
        else:
            return Response(data= serializer.errors, status=200)


class Hero(APIView):
    def get(self, request, hero_id):
        try:
            hero = HeroModel.objects.get(id = hero_id)
            serializer = HeroSerializer(hero)
            return Response(data=serializer.data, status = 200)
        except HeroModel.DoesNotExist:
            return Response(data={"mess":f"hero with id {hero_id} not found"})
    def put(self, request, hero_id):
        try:
            hero = HeroModel.objects.get(id = hero_id)
            serializer = HeroSerializer(data = request.data, instance = hero)
            if serializer.is_valid():
                hero = serializer.save()
                return Response(data={"mess": "change successfully"}, status=200)
            else:
                return Response(data= serializer.errors, status=200)
        except HeroModel.DoesNotExist:
            return Response(data={"mess":f"hero with id {hero_id} not found"})
    def delete(self, request, hero_id):
        try:
            hero = HeroModel.objects.get(id = hero_id)
            hero.delete()
            return Response(data= {"mess":"delete successfully"}, status=200)
        except HeroModel.DoesNotExist:
            return Response(data={"mess":f"hero with id {hero_id} not found"})







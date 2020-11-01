from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from .naive_bayes import NaiveBayes
import json
# Create your views here.
@csrf_exempt
def article_list(request):
    if request.method =='GET':
        articles = Article.objects.all()
        serialzer = ArticleSerializer(articles, many=True)
        return JsonResponse(serialzer.data,safe=False)
    elif request.method =='POST':
        data = JSONParser().parse(request)
        print(data)
        serialzer = ArticleSerializer(data=data)


        if serialzer.is_valid():
            serialzer.save()
            model_naive = NaiveBayes()
            arr = []
            str1 = serialzer.data['field_name']
            arr.append(str1)
            value = serialzer.data['model_name']
            sendata ={}
            for key,value in serialzer.data.items():
                sendata[key] = value
            sendata['predicted'] = str(model_naive.predictedxz(arr)[0])
            return JsonResponse(sendata,safe=False,status=201)
        return JsonResponse(serialzer.errors,status=400)
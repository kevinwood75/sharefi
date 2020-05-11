from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import datetime
from collections import OrderedDict

from fi.models import Stockinfo
from fi.serializers import FiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def fi_list(request):
    # GET list of stocks, POST a new stock, delete all stocks
    if request.method == 'GET':
        stocks = Stockinfo.objects.all()
        now = datetime.datetime.now()
        earlier = now - datetime.timedelta(days=3)
        ticker = request.GET.get('ticker', None)
        if ticker is not None:
            stocks = stocks.filter(ticker__icontains=ticker).filter(stock_date__range=(earlier,now))
        fi_serializer = FiSerializer(stocks, many=True)
        return JsonResponse(fi_serializer.data, safe=False)

    elif request.method == 'POST':
        fi_data = JSONParser().parse(request)
        fi_serializer = FiSerializer(data=fi_data)
        if fi_serializer.is_valid():
            fi_serializer.save()
            return JsonResponse(fi_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(fi_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = stocks.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def fi_detail(request,pk):
    # find turorial by (ticker)
    try:
         stocks = Stockinfo.objects.get(pk=pk)
    except Stockinfo.DoesNotExist:
        return JsonResponse({'message': 'The stock does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        fi_serializer = FiSerializer(stocks)
        return JsonResponse(fi_serializer.data)

    elif request.method == 'PUT': 
        fi_data = JSONParser().parse(request) 
        fi_serializer = FiSerializer(stocks, data=fi_data) 
        if fi_serializer.is_valid(): 
            fi_serializer.save() 
            return JsonResponse(fi_serializer.data) 
        return JsonResponse(fi_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    # GET / PUT / DELETE stock

    elif request.method == 'DELETE':
          stocks.delete()
          return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def fi_list_stock_date(request):
    # GET all published stocks
    now = datetime.datetime.now()
    earlier = now - datetime.timedelta(days=2)
    stock_records = Stockinfo.objects.filter(stock_date__range=(earlier,now)).order_by('-stock_date')
    if request.method == 'GET':
        fi_serializer = FiSerializer(stock_records,many=True)
        return JsonResponse(fi_serializer.data, safe=False)

@api_view(['GET'])
def  fi_get_ai_stock_price(request):
     if request.method == 'GET':
        stocks = Stockinfo.objects.all()
        ticker = request.GET.get('ticker', None)
        if ticker is not None:
 #          stocks = stocks.filter(ticker__icontains=ticker)
           list = []
           stocks = stocks.filter(ticker__icontains=ticker).latest('stock_date')
           result_dict = {'ticker': stocks.ticker, 'price': stocks.price, 'volume': stocks.volume, 'stock_date': stocks.stock_date}
           fi_keys = ["ticker", "price", "volume", "stock_date"]
           list_of_tuples = [(key, result_dict[key]) for key in fi_keys]
           result_dict = OrderedDict(list_of_tuples)
           list.append(result_dict)
 #       print(stocks.tickerstock_date)
 #       fi_serializer = FiSerializer(stocks, many=True)
 #       print(fi_serializer.data)
 #       ordered_d = collections.OrderedDict('ticker'=stocks.ticker, 'price'= stocks.price, 'volume'= stocks.volume, 'stock_date'=stocks.stock_date)
        print(list)
        return JsonResponse(list, safe=False)


@api_view(['GET'])
def  fi_get_av_stock_price(request):
     if request.method == 'GET':
        stocks = Stockinfo.objects.all()
#         stocks = stocks.filter(ticker__icontains=ticker)
        uniq_keys = stocks.order_by('ticker').distinct('ticker')
        print(uniq_keys)
        
#        list = []
#           stocks = stocks.filter(ticker__icontains=ticker).latest('stock_date')
#           result_dict = {'ticker': stocks.ticker, 'price': stocks.price, 'volume': stocks.volume, 'stock_date': stocks.stock_date}
#           fi_keys = ["ticker", "price", "volume", "stock_date"]
 #          list_of_tuples = [(key, result_dict[key]) for key in fi_keys]
 #          result_dict = OrderedDict(list_of_tuples)
 #          list.append(result_dict)
 #       print(stocks.tickerstock_date)
        fi_serializer = FiSerializer(stocks, many=True)
 #       print(fi_serializer.data)
 #       ordered_d = collections.OrderedDict('ticker'=stocks.ticker, 'price'= stocks.price, 'volume'= stocks.volume, 'stock_date'=stocks.stock_date)
 #       print(list)
        return JsonResponse(fi_serializer, safe=False)
 ##       return JsonResponse(list, safe=False)

from rest_framework import serializers 
from fi.models import Stockinfo
 
 
class FiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Stockinfo
        fields = ('ticker',
                  'price',
                  'volume',
                  'stock_date')
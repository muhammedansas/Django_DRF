from rest_framework import serializers
from .models import Persons,Workers

class Personserialzer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = '__all__'

    def validate(self, data):
          spl_chars = "!@#$%^&*()?/<>|[]"

          if any(c in spl_chars for c in data['name']):
               raise serializers.ValidationError("name should be not contain special charecters")
          
          if data['age'] < 18 :
               raise serializers.ValidationError("age should be greater than 18")
          
          return data
    
class Workerserialzer(serializers.ModelSerializer):
     class Meta:
          model = Workers
          fields = '__all__'
          

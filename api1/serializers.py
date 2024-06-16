from rest_framework import serializers
from .models import Tutorial2

class Tutorial2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial2
        fields = ['id','tutorialNo','title','content','StartDate']
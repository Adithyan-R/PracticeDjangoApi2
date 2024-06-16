from django.shortcuts import render

# Create your views here.

from .models import Tutorial2
from.serializers import Tutorial2Serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework  import status
from django.http import Http404

'''
class TutorialList(APIView):
    def get(self,request,format=None):
            tutorials = Tutorial2.objects.all()
            serializer = Tutorial2Serializer(tutorials, many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
        tutorials = Tutorial2.objects.all()
        serializer = Tutorial2Serializer(tutorials,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TutorialDetails(APIView):

    def get_object(self,pk):
        try:
            return Tutorial2.object.get(pk=pk)
        except Tutorial2.DoesNotExist:
            return Http404

    def get(self,request,pk,format=None):
        tutorials = self.get_object(pk)
        serializer = Tutorial2Serializer(tutorials)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        tutorials = self.get_object(pk)
        serializer = Tutorial2Serializer(tutorials,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        tutorials = self.get_object(pk)
        tutorials.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''


from rest_framework import generics


class TutorialList(generics.ListCreateAPIView):
    queryset = Tutorial2.objects.all()
    serializer_class = Tutorial2Serializer


class TutorialDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutorial2.objects.all()
    serializer_class = Tutorial2Serializer
    

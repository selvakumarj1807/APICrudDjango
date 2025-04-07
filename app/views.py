from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models import StudentEnquiry
from app.serializers import StudentEnquirySerializer
from rest_framework import viewsets, status
# Create your views here.

class StudentEnquiryViewSet(viewsets.ModelViewSet):
    queryset = StudentEnquiry.objects.all()
    serializer_class = StudentEnquirySerializer
    
    def create(self, request):
        """Create a new StudentEnquiry"""
        serializer = StudentEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Get StudentEnquiry by ID"""
        studentEnquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(studentEnquiry)
        return Response(serializer.data)
    
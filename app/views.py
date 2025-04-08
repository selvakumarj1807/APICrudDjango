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
            return Response({
                'message': 'StudentEnquiry Inserted successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Get StudentEnquiry by ID"""
        studentEnquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(studentEnquiry)
        return Response(serializer.data)
    
    def list(self, request):
        """List all StudentEnquiries with count"""
        studentEnquiries = StudentEnquiry.objects.all()
        serializer = StudentEnquirySerializer(studentEnquiries, many=True)
        return Response({
            'count': studentEnquiries.count(),
            'data': serializer.data
        })
        
    def update(self, request, pk=None):
        """Update an entire StudentEnquiry"""
        studentEnquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(studentEnquiry, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'StudentEnquiry Updated successfully',
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def destroy(self, request, pk=None):
        """Delete a StudentEnquiry"""
        studentEnquiry = get_object_or_404(StudentEnquiry, pk=pk)
        studentEnquiry.delete()
        return Response({'message': 'StudentEnquiry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


    @action(detail=False, methods=['GET'])
    def get_by_name(self, request):
        """Get StudentEnquiry by name"""
        name = request.query_params.get('name', None)
        if name is None:
            return Response({'error': 'name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        studentEnquiries = StudentEnquiry.objects.filter(name__icontains=name)
        serializer = StudentEnquirySerializer(studentEnquiries, many=True)
        return Response({
            'count': studentEnquiries.count(),
            'data': serializer.data
        })
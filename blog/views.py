from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Blog
from .serializers import BlogSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied

# Create your views here.
@swagger_auto_schema(methods=['POST'] ,
                    request_body=BlogSerializer())
@api_view(['GET', 'POST'])
def blogs(request):
    if request.method == "GET":
        songs_ = Blog.objects.all()
        serializer = BlogSerializer(songs_, many=True)
        
        data = {
           "message":"successful",
           "data": serializer.data
        }
    
    
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(): 
                
            serializer.save()
            data = {
                'message' : 'success',
                'data'  : serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            data = {
                'message' : 'failed',
                'error'  : serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    
    
    

    
    
# @swagger_auto_schema(methods=['put'] ,
#                     request_body=BlogSerializer())
# @api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def blog_detail(request, blog_id):

    
#     try:
#         song = Blog.objects.get(id=blog_id)
#     except Blog.DoesNotExist:

#         data = {
#             'message' : 'failed',
#             'error'  : f"Song with ID {blog_id} does not exist."
#         }
#         return Response(data, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = BlogSerializer(song)
        
#         data = {
#            "message":"successful",
#            "data": serializer.data
#         }
    
    
#         return Response(data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = BlogSerializer(song, data=request.data, partial=True)
#         if serializer.is_valid():
                
#             serializer.save()
#             data = {
#                 'message' : 'success',
#                 'data'  : serializer.data
#             }
#             return Response(data, status=status.HTTP_202_ACCEPTED)
#         else:
#             data = {
#                 'message' : 'failed',
#                 'error'  : serializer.errors
#             }
#             return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method=="DELETE":
#         song.delete()
        
#         return Response({}, status=status.HTTP_204_NO_CONTENT)
    



# @swagger_auto_schema(methods=['POST'] ,
#                     request_body=PlayListSerializer())
# @api_view(['GET', 'POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def playlists(request):
#     user= request.user
#     if request.method == "GET":
#         playlist_ = PlayList.objects.filter(user=user)
#         serializer = PlayListSerializer(playlist_, many=True)
        
#         data = {
#            "message":"successful",
#            "data": serializer.data
#         }
    
    
#         return Response(data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = PlayListSerializer(data=request.data)
#         if serializer.is_valid(): 
#             if "user" in serializer.validated_data.keys():
#                 serializer.validated_data.pop("user")
#             # print(serializer.validated_data)  
#             song = serializer.validated_data["song"]
            
#             # print(song)
#             play_list = PlayList.objects.create(user=user, song=song)
#             new_serializer = PlayListSerializer(play_list)
            
#             data = {
#                 'message' : 'success',
#                 'data'  : new_serializer.data
#             }
#             return Response(data, status=status.HTTP_202_ACCEPTED)
#         else:
#             data = {
#                 'message' : 'failed',
#                 'error'  : serializer.errors
#             }
#             return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    
    
    

    
    

# @api_view(['GET', 'DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def blog_detail(request, item_id):

    
#     try:
#         song = PlayList.objects.get(id=item_id)
#     except PlayList.DoesNotExist:

#         data = {
#             'message' : 'failed',
#             'error'  : f"Playlist with ID {item_id} does not exist."
#         }
#         return Response(data, status=status.HTTP_404_NOT_FOUND)
#     if song.user != request.user:
#         raise PermissionDenied(detail={"message":"You do not have the permission to view this item."})
    
#     if request.method == "GET":
#         serializer = PlayListSerializer(song)
        
#         data = {
#            "message":"successful",
#            "data": serializer.data
#         }
    
    
#         return Response(data, status=status.HTTP_200_OK)
    
#     elif request.method=="DELETE":
#         song.delete()
        
#         return Response({}, status=status.HTTP_204_NO_CONTENT)
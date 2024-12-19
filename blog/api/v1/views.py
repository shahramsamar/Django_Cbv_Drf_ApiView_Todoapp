
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class PostList(APIView):
#     """ getting a list of post and creating new posts"""
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    """ retrieving a list of posts"""
    def get(self,request):
            post = Post.objects.filter(status=True)
            serializer = PostSerializer(post,many=True)
            return Response(serializer.data)
        
    """creating a post with provided data"""
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
           



@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, id):
   
    # try:
    #     post = Post.objects.get(pk=id)
    #     # print(post.__dict__)
    #     serializer = PostSerializer(post)
    #     # print(serializer.__dict__)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     # return Response({'detail':'post dose not exist'},status=404)
    #     return Response({'detail':'post dose not exist'},status=status.HTTP_404_NOT_FOUND)

    # Get the post object or return a 404 error if not found
    post = get_object_or_404(Post, pk=id, 
                                        status=True)

    # Handle GET request
    if request.method == 'GET':

        # Serialize the post object
        serializer = PostSerializer(post)
        
        # Return the serialized data as a response
        return Response(serializer.data)

        # Handle PUT request
    elif request.method == 'PUT':
        # Create a serializer instance with the request data
        serializer = PostSerializer(post,
         data=request.data)
        # Validate the serializer data
        if serializer.is_valid(raise_exception=True):
        # Save the new post
            serializer.save()
        #  Return the serialized data of the new post
        return Response(serializer.data)

     # Handle DELETE request
    elif request.method == 'DELETE':  
        post.delete()  
        #  Return the serialized data of the new post
        return Response({'detail':'item removed successfully'}, 
                                     status=status.HTTP_204_NO_CONTENT)
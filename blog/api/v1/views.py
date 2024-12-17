
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
 


@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    # Handle GET request
    if request.method == 'GET':
        # Retrieve all active posts
        posts = Post.objects.filter(status=True)
        # Serialize the queryset of posts
        serializer = PostSerializer(posts, many=True)
        # Return serialized data as response
        return Response(serializer.data)
    
    # Handle POST request
    elif request.method == 'POST':
        # return Response("ok")
        # return Response(request.data)

        # Create a serializer instance with the request data
        serializer = PostSerializer(data=request.data)
        # Validate the serializer data
        if serializer.is_valid(raise_exception=True):
        # Save the new post
            serializer.save()
        # Return the serialized data of the new post
            return Response(serializer.data)

        # if serializer.is_valid():
        # #     # Save the new post
        #     serializer.save()
        # #     # Return the serialized data of the new post
        #     return Response(serializer.data)
        # else:
        #     # Return serializer errors if data is invalid
        #     return Response(serializer.errors)



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
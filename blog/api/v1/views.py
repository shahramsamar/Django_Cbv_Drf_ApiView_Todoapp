
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
           


class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it"""
    permission_classes =[IsAuthenticated]
    serializer_class = PostSerializer
    
    """retrieving the post data"""
    def get(self,request,id):
        post =  get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    """editing the post data"""
    def put(self,request,id):
        post =  get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    """ deleting the post object """
    def delete(self,request,id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
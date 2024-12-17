from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from blog.forms import PostForm
from blog.models import Post
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView )




"""
PostListView:
    - A class-based view to display a list of all blog posts.
    - Uses the 'blog/post-list.html' template to render the list.
    - The context variable for posts is 'posts'.
    - The posts are ordered by the 'id' field in descending order.
    - Pagination can be enabled by setting 'paginate_by'.
"""  
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/post_list.html"  
    context_object_name = "posts"
    ordering = ("-id")
    # paginate_by = 1

"""
PostDetailView:
    - A class-based view to display details of a specific blog post.
    - Uses the 'blog/post-detail.html' template for rendering.
    - Displays detailed information for a single post instance.
"""
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"   
             
"""
PostCreateView:
    - A class-based view to handle the creation of new blog posts.
    - Renders a form to create a post with fields: 'title', 'content', 'status', and 'published_date'.
    - Upon successful creation, the user is redirected to the homepage ("/").
    - Uses the 'blog/post-form.html' template for the form rendering.
"""
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title','content']
    success_url = '/'
    template_name = "blog/post_form.html" 
    
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    '''
    a class  based UpdateView to show post_form page
    '''  
    model = Post 
    form_class = PostForm
    success_url = '/'    
    template_name = "blog/post_form.html" 


class PostDeleteView(LoginRequiredMixin, DeleteView):
    '''
    a class  based DeleteView to show post_form page
    '''  
    model = Post 
    success_url = '/'
    template_name = "blog/post_confirm_delete.html" 
    
class PostDoneView(LoginRequiredMixin, View):  
    '''
    a class  based DoneView to done post in page
    '''  
    model = Post
    success_url = "/"
    def get(self,request,*args,**kwargs):
        # print('post id :',kwargs["pk"])
        post = get_object_or_404(Post,pk=kwargs['pk'])
        post.status = True
        post.save()
        # print('post status update')
        return redirect(self.success_url)
  


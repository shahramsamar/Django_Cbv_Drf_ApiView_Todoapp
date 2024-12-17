from django.contrib import admin
from blog.models import Post




"""
PostAdmin:
    - This class customizes the admin interface for the Post model.
    - `list_display`: Specifies the fields to be displayed in the admin list view for posts.
        - `title`: The title of the post.
        - `status`: Shows whether the post is published or in draft mode (Boolean).
        - `created_date`: Displays the date and time when the post was created.
        - `published_date`: Displays the date and time when the post was published.
"""
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_date']



# Register the Post model with its custom admin interface.

admin.site.register(Post, PostAdmin)
from django.contrib import admin
from .models import Post
from .models import Register
from .models import Contact_Us


admin.site.register(Post)
admin.site.register(Register)
admin.site.register(Contact_Us)

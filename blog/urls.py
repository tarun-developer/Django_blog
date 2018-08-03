from django.conf.urls import url, include

from django.views.generic import ListView, DetailView
from blog.models import Details

urlpatterns = [ 
                url('^$', ListView.as_view(queryset = Details.objects.all().order_by("-date")[:25],template_name="blog/blog.html")),
               
               
                url('^(?P<pk>\d+)$', DetailView.as_view(model = Details,template_name="blog/post.html")),
      
              ]
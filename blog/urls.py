from . import views
from django.urls import path

# This is similar to what you have done before. However, because we are
# using class-based views, we need to add the 'as_view' method at the
# end of 'PostList'. So, it is going to render this class as a view:
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]

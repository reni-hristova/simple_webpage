from django.urls    import path
from .              import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv_template/', views.cv, name="cv"),
    path('cv/entry/new/', views.entry_new, name='entry_new'),
    path('cv/entry/<int:pk>/', views.entry_details, name='entry_details'),
    path('cv/entry/<int:pk>/edit/', views.entry_edit, name='entry_edit'),
    path('cv/', views.entry_list, name='entry_list'),
#    path('cv/personalprofile/', views.personalprofile, name = 'personalprofile'),
#    path('cv/personalprofile/edit', views.personalprofile_edit, name = 'personalprofile_edit'),


]

#<int:pk> – integer expected that will transfer to a view as a variable called pk (primary key)

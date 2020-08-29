from django.urls    import path
from .              import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv/', views.cv, name="cv"),
    path('entry/new/', views.entry_new, name='entry_new'),
    path('entry/<int:pk>/', views.entry_details, name='entry_details'),
    path('entry/<int:pk>/edit/', views.entry_edit, name='entry_edit'),
    path('cv_all/', views.entry_list, name='entry_list'),

]

#<int:pk> – integer expected that will transfer to a view as a variable called pk (primary key)

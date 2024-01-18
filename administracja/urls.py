from django.urls import path, include,reverse
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from . import views
app_name='administracja'
urlpatterns=[
    #path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(success_url = reverse_lazy('administracja:password_change_done')), name='password_change_done'),

    
    path('login/',auth_views.LoginView.as_view(),name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('',views.dashboard,name="dashboard"),
    path('',views.index,name="index"),
    path('',views.lista_lekarzy,name="lista_lekarzy"),
    path('lista_lekarzy',views.lista_lekarzy,name="lista_lekarzy"),
    path('register/',views.register,name="register"),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url='done'), name='password_change'),
    
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
        path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
        name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
        name='product_detail'),
   
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
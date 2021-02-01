from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('test/',views.log),
    path('adduser/',views.adduserindatabase, name="adduser"),
    path('test/delete/<int:pk>/',views.delete_user),
    path('test/session/<int:pk>/',views.session_end),
    path('test/post_community/',views.add_post_and_show_it,name="addpostandshowit")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
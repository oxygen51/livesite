from django.urls import path
from portfolio import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home.as_view(), name="home" ),
    path('blog/', views.blog, name="blog" ),
    path('publication/', views.publication, name="publication"),
    path('contact/', Contact.as_view(), name="contact"),
    path('history/', History.as_view(), name="history"),
    path('achievement/', Achievement.as_view(), name="achievement"),
    path('project/', views.project, name="project" ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
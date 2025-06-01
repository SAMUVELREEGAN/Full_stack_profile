from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
      path('api/landingpara/', include('landing.urls')),
      path('api/about/', include('about.urls')),
      path('api/detail/', include('detail.urls')),
      path('api/education/', include('education.urls')),
      path('api/experience/', include('experience.urls')),
      path('api/mycontact/', include('contact.urls')),
      path('api/projects/', include('project.urls')),
      path('api/questions/', include('questions.urls')),
      path('api/scroll/', include('scroll.urls')),
      path('api/services/', include('services.urls')),
      path('api/myskills/', include('myskill.urls')),
      path('api/visitors/', include('visitors.urls')),
      path('api/', include('feedback.urls')),
      path('api/', include('projesturl.urls')),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

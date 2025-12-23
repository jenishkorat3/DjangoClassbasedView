from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('template/', include('templateview.urls')),
    path('redirect/', include('redirectview.urls')),
    path('list/', include('genericclasslistview.urls')),
    path('detail/', include('genericclassdetailview.urls')),
    path('form/', include('formview.urls')),
    path('create/', include('createview.urls')),
]

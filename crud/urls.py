
from django.contrib import admin
from django.urls import path
from crud_app.views import Create, GetAll, Update, Delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/<user_id>', Create.as_view(), name='create'),
    path('get_all', GetAll.as_view(), name='get-all'),
    path('update/<id>', Update.as_view(), name='update'),
    path('delete/<id>', Delete.as_view(), name='delete')
]

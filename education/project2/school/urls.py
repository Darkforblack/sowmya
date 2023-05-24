
from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   #path('', include('school.urls')),
    path('abc/',views.abc, name='abc'),
    path('',views.index, name='index'),
    path('register/',views.register, name='register'),
    # path('handelelogin/register/',views.register, name='handelelogin/register'),
    path('loginn',views.loginn, name='loginn'),
    path('dash/',views.dash, name='dash'),
    path('students/',views.students, name='students'),
    path('teacher/',views.teacher, name='teacher'),

]
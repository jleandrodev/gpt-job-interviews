from django.urls import path
from .views import list_jobs, job_details

app_name = 'jobs'

urlpatterns = [
    path('', list_jobs, name='list'),
    path('<int:pk>', job_details, name='details')
]
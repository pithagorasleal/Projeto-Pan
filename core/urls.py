from django.urls import path, re_path
from core.views import *

urlpatterns = [
    path('', login, name='login'),
    path('index/', index, name='index'),
    path('step/new', step_new, name='step_new'),
    path('process/new', process_new, name='process_new'),
    re_path(r'^process/(?P<process_id>\d+)$', process_config, name='process_config'),
    re_path(r'^process/(?P<process_name>\w+)/config$', process_config_new, name='process_config_new'),
    re_path(r'^process/(?P<process_name>\w+)/config/(?P<processstep_id>\d+)/$', process_config_step, name='process_config_step'),
    re_path(r'^delete/(?P<process_step_id>\d+)/$', deleteStepFromConfig ,name='process_step_delete'),
]
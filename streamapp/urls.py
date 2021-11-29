from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('view_employee/<int:id>/', views.viewemp, name='viewemp'),
    path('addemployee/', views.addemp, name='addemp'),
    path('employee_list/', views.emplist, name='emplist'),
    path('show/<int:id>/', views.show, name='show'),
    path('showun/<int:id>/', views.showun, name='showun'),
    path('configuration_cam_no1', views.configuration,name='configuration'),
    path('configuration_cam_no2', views.configuration2,name='configuration2'),
    path('report', views.report, name='report'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    #path('mask_feed', views.mask_feed, name='mask_feed'),
	path('livecam_feed', views.livecam_feed, name='livecam_feed'),
    ]

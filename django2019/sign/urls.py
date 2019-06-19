from django.urls import path

from sign.views import views_if

urlpatterns = [
# guest system interface:
# ex : /api/add_event/
path('add_event/', views_if.add_event, name='add_event'),
# # ex : /api/add_guest/
# path(r'^add_guest/', views_if.add_guest, name='add_guest'),
# # ex : /api/get_event_list/
# path(r'^get_event_list/', views_if.get_event_list, name='get_event_list'),
# # ex : /api/get_guest_list/
# path(r'^get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
# # ex : /api/user_sign/
# path(r'^user_sign/', views_if.user_sign, name='user_sign'),
]
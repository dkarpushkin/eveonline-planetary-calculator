from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PiCalculaotorView.as_view(template_name='pi_calc.html'), name='pi_calculator_main')
]

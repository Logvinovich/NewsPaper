from django.urls import path
from appointments.views import Appointment

urlpatterns = [
        path('', Appointment.as_view(), name='make_appointment'),

]
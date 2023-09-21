from datetime import datetime
from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class Appointment(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )


        html_content = render_to_string(
            'appointment_created.html',
            {
                'appointment': appointment,
            }
        )


        # отправляем письмо
        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            body=appointment.message,
            from_email='demon.k1ller@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
            to=['piter_pen1999@mail.ru',]  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()

        return redirect('appointments:make_appointment')



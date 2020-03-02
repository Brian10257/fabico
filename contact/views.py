from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        subject = request.POST['subject']
        user_id = request.POST['user_id']

        contact = Contact(name=name, email=email, phone=phone, message=message, subject=subject, user_id=user_id)
        contact.save()

        # Send Mail
        if request.user.is_authenticated:
            subject = "Message Subject: " + subject
        else:
            subject = "A Visitor: Message Subject; " + subject

        message = "Mr/Miss  " + name + " With The Email: " + email + " And Phone Number: "+phone + ", Deposited A Job Application On The School WebSite" + \
            "\n\n" + message 
        "\n\n\n Contact The Web Master For More Information On This Applicaton And Also To Access The Applicant's Files."
        send_mail(subject, message, 'wgrealestate21@gmail.com', ['ntschangb@yahoo.com', 'ntschangb@gmail.com'], [''])

        messages.success(request, 'Your Message Was Successfuly Sent, We Will Get Back To You Soon')
        return redirect('contact')

    return render(request, 'contacts/contact.html')

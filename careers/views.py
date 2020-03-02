from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from .models import Career
from .forms import CareerForm


def career(request):
    if request.method == 'POST':
        name = request.POST['name']
        career_form = CareerForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_upload')
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        place_of_birth = request.POST['place_of_birth']
        current_city = request.POST['current_city']
        neighbour_hood = request.POST['neighbour_hood']
        current_employment = request.POST['current_employment']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']
        if career_form.is_valid():
            for f in files:
                file_instance = Career(file_upload=f, name=name, email=email, phone_number=phone_number, place_of_birth=place_of_birth, current_city=current_city, current_employment=current_employment, neighbour_hood=neighbour_hood,subject=subject, message=message, user_id=user_id)
                file_instance.save()

        # Send Mail
        if request.user.is_authenticated:
            subject = "Message Subject: " + subject
        else:
            subject = "A Visitor: Message Subject; " + subject

        message = "Mr/Miss  " + name + " With The Email: " + email + " And Phone Number: "+phone_number + ", Deposited A Job Application On The School WebSite" + "\n\n" + message + str(files) 
        "\n\n\n Contact The Web Master For More Information On This Applicaton And Also To Access The Applicant's Files."
        send_mail(subject, message, 'wgrealestate21@gmail.com', ['ntschangb@yahoo.com', 'ntschangb@gmail.com'], [''])

        messages.success(request, 'Your Application Has Been Recieved, We Will Get Back To You Soon')
        return redirect('career')

    return render(request, 'careers/careers.html')

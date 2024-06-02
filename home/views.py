from django.shortcuts import render 
from django.contrib import messages
from .models import Doctor,Patient,Booking
from twilio.rest import Client


# Create your views here.
# def home(request):
#     if request.method == 'POST':
#         pname = request.POST.get('pname')
#         dname = request.POST.get('dname')
#         date = request.POST.get('date')
#         patient = patient.objects.get(name=pname)
#         doctor = doctor.objects.get(name=dname)
#         db = Booking()
#         db.patientsname = patient
#         db.Docname = doctor
#         db.book_id = 1
#         db.date = date
#         db.save()
#         messages.success(request, "Appointment booked!!!")
    
#     return render(request, 'home.html')
# Your Twilio account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Your Twilio WhatsApp-enabled number
twilio_whatsapp_number = 'whatsapp:+14155238886'
def home(request):
    data=Booking.objects.all()
    if request.method == 'POST':
        pname = request.POST.get('pname')
        dname = request.POST.get('dname')
        date = request.POST.get('date')
        phone_number = request.POST.get('phone_number')
        
        try:
            patient, created = Patient.objects.get_or_create(name=pname)
            if created:
                messages.success(request, "New patient created.")
            doctor = Doctor.objects.get(name=dname)
            
            booking = Booking()
            booking.patient = patient
            booking.doctor = doctor
            booking.date = date
            booking.status = True  # Default status or you can change based on your logic
            booking.save()
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f'Appointment booked! \nPatient: {pname}\nDoctor: {dname}\nDate: {date}',
                from_=twilio_whatsapp_number,
                to=f'whatsapp:+91{phone_number}'  # Ensure the phone number is in the correct format
            )
            
            messages.success(request, "Appointment booked!!! WhatsApp message sent.")
            
            messages.success(request, "Appointment booked!!!")
        except Patient.DoesNotExist:
            messages.error(request, "Patient does not exist.")
        except Doctor.DoesNotExist:
            messages.error(request, "Doctor does not exist.")
    
    return render(request, 'home.html',{"datas":data})

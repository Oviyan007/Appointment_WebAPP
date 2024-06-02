
# Django Appointment Booking System

This is a simple Django-based appointment booking system where patients can book appointments with doctors. The system also sends a confirmation message to the patient's WhatsApp number using Twilio.

## Features

- Book appointments with doctors
- Store patient and doctor details
- Send appointment confirmation to patient's WhatsApp number

## Prerequisites

- Python 3.8+
- Django 3.2+
- Twilio account
---
# Screenshots

---
#![Screenshot 2024-06-03 002409](https://github.com/Oviyan007/Appointment_WebAPP/assets/86316218/6a689079-e7e3-4938-8aee-7f505c55448b)
---
![Screenshot 2024-06-03 002637](https://github.com/Oviyan007/Appointment_WebAPP/assets/86316218/12bed405-0bb9-4f9a-8fae-dc51424c9024)

---

## Setup

### Step 1: Clone the repository

```
git clone https://github.com/Oviyan007/Appointment-App.git
cd appointment-booking-system
```
### Step 2: Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows use
venv\Scripts\activate
```

### Step 3: Install require packages 
```
pip install django
pip install twilio
```
### Step 4: Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
### Step 5: create super user
```
python manage.py createsuperuser
```
### Step 6: configure twilio 

  - Signup[Twilio](https://www.twilio.com/en-us)
  - goto the try it out section and select the whatsapp message and create the sandbox
  - open console or click the logo in top left corner you can see the SID and Auth token copy that
  - In the whatsapp sandbox you can see the whatsapp number copy that
  - paste those details in views.py file
### Step 7:Start the developement server
```
python manage.py runserver
```
### Step 8:Acces the webApplication 
Open your web browser and go to http://127.0.0.1:8000/.

### Usage
- Enter the patient's name.
- Enter the doctor's name.
- Choose the date for the appointment.
- Enter the patient's WhatsApp number.
- Click "Submit".

from django.db import models

# Create your models here.
# class doctor(models.Model):
#     name=models.TextField(max_length=100,null=False)
#     Doc_id=models.IntegerField(null=False)
#     Specialist=models.TextField(max_length=100,null=False)
# class patients(models.Model):
#     patientsname=models.TextField(max_length=100,null=False)
#     patient_id=models.IntegerField(null=False)
# class Booking(models.Model):
#     patientsname=models.ForeignKey(patients,on_delete=models.CASCADE)
#     book_id=models.IntegerField(null=False)
#     Docname=models.ForeignKey(doctor,on_delete=models.CASCADE)
#     status=models.BooleanField()
#     date=models.DateField(null=True)
class Doctor(models.Model):
    name = models.CharField(max_length=100, null=False)
    doc_id = models.AutoField(primary_key=True)  # Using AutoField for primary key
    specialist = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name +"--------"+ self.specialist

class Patient(models.Model):
    name = models.CharField(max_length=100, null=False)
    patient_id = models.AutoField(primary_key=True)  # Using AutoField for primary key
 
class Booking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateField(null=True)
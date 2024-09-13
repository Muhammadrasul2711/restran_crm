from django.db import models
from django.contrib.auth.models import User





class Position(models.Model):
    full_name= models.CharField(max_length=255)


    def __str__(self):
        return self.full_name



class Staff(models.Model):
    full_name= models.CharField(max_length=255)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)
    email= models.EmailField()
    phone= models.CharField(max_length=13)
    is_active= models.BooleanField(default=True)


    def __str__(self):
        return self.full_name

class SHift(models.Model):
    full_name= models.CharField(max_length=255)
    start_time= models.TimeField()
    end_time= models.TimeField()


    def __str__(self):
        return self.full_name


class StaffSHift(models.Model):
    staff= models.ForeignKey(Staff,on_delete=models.CASCADE)
    shift= models.ForeignKey(SHift,on_delete=models.CASCADE)
    data=models.DateTimeField()

    def __str__(self):
        return f"{self.staff} - {self.shift} on {self.date}"



class StaffAttendance(models.Model):
    staff_shift = models.ForeignKey(StaffSHift, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(blank=True, null=True)
    check_out_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Attendance for {self.staff_shift.staff} on {self.staff_shift.date}"


















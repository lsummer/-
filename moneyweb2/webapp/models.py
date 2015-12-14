from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=30)  
    password = models.CharField(max_length=30)  

class Salary(models.Model):
    post_name = models.CharField(max_length=10) 
    base = models.FloatField()                  
    
class People(models.Model):
    username1 = models.ForeignKey(Users)      
    name = models.CharField(max_length=30)    
    nation = models.CharField(max_length=7)   
    sex = models.BooleanField(default=True)   
    phone = models.CharField(max_length=11)   
    email = models.EmailField()               
    address = models.CharField(max_length=50) 
    birthday = models.DateField()             
    date = models.DateField()                 
    postkey = models.ForeignKey(Salary)          
        
class Full_salary(models.Model):
    peopleid = models.ForeignKey(People)   
    datemonth = models.CharField(max_length=7)  
    tsavings = models.FloatField()              
    zsavings = models.FloatField()              
    base = models.FloatField()                  
    all_salary = models.FloatField()        

class Yewu(models.Model):
    username1 = models.ForeignKey(Users) 
    title = models.CharField(max_length=50)
    client = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    zhishou = models.BooleanField(default=True)
    money = models.FloatField()
    person = models.CharField(max_length=30)
    date = models.DateField()
    checkinDate = models.DateField()
    beizhu = models.CharField(max_length=100)

class huowu(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    danwei = models.CharField(max_length=50)
    number = models.IntegerField(max_length = 20)
    preprice = models.FloatField()
    allprice = models.FloatField()
    shuilv = models.FloatField()
    shuie = models.FloatField()
    
    
class Bill(models.Model):
    username1 = models.ForeignKey(Users) 
    aman = models.CharField(max_length=50)
    bman = models.CharField(max_length=50)
    
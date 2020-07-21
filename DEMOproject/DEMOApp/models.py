from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class customerscore(models.Model):
    customernumber = models.CharField(max_length=122)
    cstscor = models.IntegerField()

    def __str__(self):
        return self.customernumber

#rating_choices = (('Completely', 'completely'),('Very well', 'very well'),('Somewhat', 'somewhat'),('Very little', 'very little'),('Not at all', 'not at all'))
#accounts_choices = (('Always', 'always'),('Often','often'),('Sometimes','sometimes'),('Rarely','rarely'),('Never','never'))

class surveyscore(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    scores = models.IntegerField(default=0)
    #major = models.CharField(max_length=122, choices=rating_choices)
    #accounts = models.CharField(max_length=122, choices=accounts_choices)
    #details = models.CharField(max_length=122)

    def __str__(self):
        return self.name

class accountids:
    actid : str
    schname : str
    actname : str
    descname : str
    curr : str
    acttyp : str
    actsubtyp : str
    accountids : str


class balances:
    balactid : str
    cdamount : float
    cdcurrency: str
    cdindicator : str
    bdtime : str
    balamt : float
    debtbuddyflag: str



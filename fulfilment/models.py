from django.db import models
from django.contrib.auth.models import User
from registration.models import CharityNames

class FulfilmentType(models.Model):
    charity_name    = models.ForeignKey(CharityNames, on_delete= models.DO_NOTHING)
    file_type       = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.charity_name

    def __str__(self):
        return self.file_type


class UploadFile(models.Model):
    upload_date     = models.DateField(auto_now_add=True, blank=True, null=True)
    file_name       = models.CharField(max_length=100, blank=True, null=True)
    user_id         = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    file_path       = models.FileField(upload_to='data')
    charity_name    = models.ForeignKey(CharityNames, on_delete= models.DO_NOTHING)
    file_type       = models.ForeignKey(FulfilmentType, on_delete= models.DO_NOTHING, null=True)

    def __str__(self):
        return self.file_name

    def __str__(self):
        return self.user_id


class DownloadFile(models.Model):
    merge_date      = models.DateField(auto_now_add=True, blank=True, null=True)
    date_from       = models.DateField()
    date_to         = models.DateField()
    user_id         = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    charity_name    = models.ForeignKey(CharityNames, on_delete= models.DO_NOTHING)

    def __str__(self):
        return self.charity_name

    def __str__(self):
        return self.user_id


class FulfilmentFilesData(models.Model):
    upload_date             = models.DateField(auto_now_add=True, blank=True, null=True)
    charity_name            = models.ForeignKey(CharityNames, on_delete= models.DO_NOTHING)
    urn                     = models.CharField(max_length=100, null=True)
    title                   = models.CharField(max_length=100, null=True)
    firstname               = models.CharField(max_length=100, null=True)
    midname                 = models.CharField(max_length=100, null=True)
    surname                 = models.CharField(max_length=100, null=True)
    add1                    = models.CharField(max_length=100, null=True)
    add2                    = models.CharField(max_length=100, null=True)
    add3                    = models.CharField(max_length=100, null=True)
    add4                    = models.CharField(max_length=100, null=True)
    add5                    = models.CharField(max_length=100, null=True)
    town                    = models.CharField(max_length=100, null=True)
    county                  = models.CharField(max_length=100, null=True)
    postcode                = models.CharField(max_length=100, null=True)
    country                 = models.CharField(max_length=100, null=True)
    card_holders_name       = models.CharField(max_length=100, null=True)
    bank_account_number     = models.IntegerField(null=True)
    giftaid_decl            = models.CharField(max_length=100, null=True)
    frequency               = models.CharField(max_length=100, null=True)
    first_collection_date   = models.CharField(max_length=100, null=True)
    amount                  = models.DecimalField(decimal_places=2, max_digits=10, null=True)

    def __str__(self):
        return self.file_name

    def __str__(self):
        return self.urn

    def __str__(self):
        return self.title

    def __str__(self):
        return self.firstname

    def __str__(self):
        return self.midname
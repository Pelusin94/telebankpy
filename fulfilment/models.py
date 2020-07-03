from django.db import models

class UploadFile(models.Model):
    upload_date     = models.DateField(auto_now_add=True, blank=True, null=True)
    file_name       = models.CharField(max_length=100, blank=True, null=True)
    user_id         = models.CharField(max_length=100, blank=True, null=True)
    file_path       = models.FileField(upload_to='data')

    def __str__(self):
        return self.upload_date

    def __str__(self):
        return self.file_name

    def __str__(self):
        return self.user_id

    def __str__(self):
        return self.file_path

class DownloadFile(models.Model):
    merge_date      = models.DateField(auto_now_add=True, blank=True, null=True)
    date_from       = models.DateField()
    date_to         = models.DateField()
    user_id         = models.CharField(max_length=100, blank=True, null=True)
    charity_name    = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.merge_date

    def __str__(self):
        return self.date_from

    def __str__(self):
        return self.date_to


class FulfilmentFilesData(models.Model):
    charity_name            = models.CharField(max_length=100, null=True)
    file_name               = models.CharField(max_length=100, null=True)
    upload_date             = models.DateField(auto_now_add=True)
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
        return self.upload_date

    def __str__(self):
        return self.urn

    def __str__(self):
        return self.title

    def __str__(self):
        return self.firstname

    def __str__(self):
        return self.midname
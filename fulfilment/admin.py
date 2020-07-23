from django.contrib import admin
from . import models


admin.site.register(models.FulfilmentFilesData)
admin.site.register(models.DownloadFile)
admin.site.register(models.UploadFile)
admin.site.register(models.FulfilmentType)

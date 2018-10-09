# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mentor(models.Model):
    nama = models.CharField(max_length=200)
    asal_kota = models.CharField(max_length=200)
    mata_pelajaran = models.ForeignKey('mata_pelajaran.MataPelajaran',null=True, on_delete= models.CASCADE)

    def __str__(self):
        return self.nama
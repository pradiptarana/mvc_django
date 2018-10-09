# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=200)
    jadwal_mulai = models.DateTimeField()
    jadwal_berakhir = models.DateTimeField()

    def __str__(self):
        return self.nama_pelajaran
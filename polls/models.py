# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fiction(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    last_update_time = models.DateTimeField(blank=True, null=True)
    desc = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    convert = models.CharField(max_length=255, blank=True, null=True)
    latest_chapter = models.CharField(max_length=255, blank=True, null=True)
    class_id = models.ForeignKey('FictionClass', blank=True, null=True, db_column='class_id', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'fiction'


class FictionChapter(models.Model):
    # fiction_id = models.IntegerField(null=True, blank=True)
    fiction_id = models.ForeignKey(Fiction, on_delete=models.CASCADE, null=True, blank=True, db_column='fiction_id')
    chapter = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    sort_id = models.IntegerField(auto_created=True, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'fiction_chapter'


class FictionClass(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fiction_class'

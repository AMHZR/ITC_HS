from django.db import models
from tagging.registry import register as tagging_register

class Category(models.Model):
    category = models.CharField(max_length=1000,null=False,blank=False)

    def __unicode__(self):
        return "%s"%(self.category)

class Sub_Category(models.Model):
    desc = models.TextField(max_length=1000)
    cat = models.ForeignKey(Category)

    def __unicode__(self):
        return "%s"%(self.desc)


class Note(models.Model):
    note_id = models.CharField(max_length=10,blank=False)
    desc = models.TextField(blank=False)

    def __unicode__(self):
        return "Note %s"%(self.note_id)

class Section(models.Model):
    section_id = models.IntegerField(unique=True,null=False,blank=False)
    name = models.CharField(max_length=300, verbose_name='Section Name', null=False, blank=False)

    def __unicode__(self):
        return "%s %s"%(self.section_id,self.name)

class Chapter(models.Model):
    chapter_id = models.IntegerField(unique=True,null=False,blank=False)
    name = models.CharField(max_length=300, verbose_name='Chapter Name', null=False, blank=False)
    section = models.ForeignKey(Section,blank=False,null=False)
    notes = models.ManyToManyField(Note,blank=True)

    def __unicode__(self):
        return "%s %s"%(self.chapter_id, self.name)

class Article(models.Model):
    code = models.IntegerField()
    heading = models.CharField(max_length=1000)
    chapter = models.ForeignKey(Chapter)

    def __unicode__(self):
        return "%s  %s"%(self.code,self.heading)

    class Meta:
        ordering = ['id']

class hscode(models.Model):
    hs = models.CharField(max_length=20,verbose_name="HS-CODE")
    desc = models.TextField(verbose_name="HSCODE description")
    article = models.ForeignKey(Article)
    wef = models.DateField(auto_now=True, verbose_name='W.E.F', blank=True)
    policy = models.CharField(max_length=30,verbose_name="Policy Restriction")

    hs_5 = models.CharField(max_length=800,  blank=True)
    hs_6 = models.CharField(max_length=800,  blank=True)
    hs_8 = models.CharField(max_length=1000, blank=True)

    condition = models.CharField(max_length=1000, blank=True)
    note = models.ManyToManyField(Note, blank=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.hs

tagging_register(hscode)
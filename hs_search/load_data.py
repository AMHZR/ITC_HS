__author__ = 'aamir'
import csv
from models import Article, Chapter,Category,Sub_Category,hscode,Section

path = '/Users/aamir/work/Delhivery/hscodes/hs_search/datafile.csv'
error_rows = []


# def load_data():
#     with open(path) as f:
#         reader = csv.reader(f)
#
#         for row in reader:
#             try:
#                 code = itc_hscode()
#                 code.itc_hs = row[0]
#                 code.desc = row[1]
#
#                 code.hs4, created = itc_hs4.objects.get_or_create(desc=row[2])
#                 code.hs5, created = itc_hs5.objects.get_or_create(desc=row[3])
#                 code.hs6, created = itc_hs6.objects.get_or_create(desc=row[4])
#                 code.hs8, created = itc_hs8.objects.get_or_create(desc=row[5])
#
#                 code.policy = row[6]
#                 code.condition = row[7]
#                 code.save()
#             except:
#                 print 'errorrrrrrrrr', row[0]
#                 error_rows.append(row[0])


chapter_path = "/Users/aamir/Downloads/new_data.csv"

def load_sections():
    with open(chapter_path , mode='rU') as f:
        reader = csv.reader(f)
        i=1
        for row in reader:
            try:
                if row[3]:
                    obj, created = Section.objects.get_or_create(section_id=row[2])
                    obj.name = row[3]
                    obj.save()
            except Exception as e:
                print 'Error Creating Section',e

def load_chapters():
    with open(chapter_path , mode='rU') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                section = Section.objects.get(section_id=row[2])
                obj, created = Chapter.objects.get_or_create(chapter_id=row[0],section=section)
                if row[1]:
                    obj.name = row[1]
                else:
                    obj.name = row[5]
                obj.save()
            except:
                print 'Error Creating Chapter'

def load_categories():
    with open(chapter_path , mode='rU') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                obj, created = Category.objects.get_or_create(category=row[4])
                obj.save()
            except:
                print 'Error Creating Category'

def load_sub_categories():
    with open(chapter_path , mode='rU') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                cat = Category.objects.get(category=row[4])
                print cat.category
                obj, created = Sub_Category.objects.get_or_create(desc=row[5],cat=cat)
                obj.save()
            except Exception as e:
                print 'Error Creating  SubCategory'
                print e

def load_articles():
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                chapter = Chapter.objects.get(chapter_id=int(row[0][:2]))
                article, created = Article.objects.get_or_create(code=row[0][:4],chapter=chapter)
                article.heading = row[2]
                article.save()
            except Exception as e:
                print 'Error Loading Articles'
                print e

def load_hscodes():
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                article = Article.objects.get(code=row[0][:4])
                hs_code = hscode(hs=row[0])
                hs_code.desc = row[1]
                hs_code.article = article
                hs_code.policy = row[6]
                hs_code.hs_5 = row[3]
                hs_code.hs_6 = row[4]
                hs_code.hs_8 = row[5]
                hs_code.condition = row[7]
                hs_code.save()
            except Exception as e:
                print 'Error Loading HS code'
                print e
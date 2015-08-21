#!/usr/bin/python
__author__ = 'aamir'
import xml.etree.cElementTree as ET
from models import *

def generate_solr_xml():
    root = ET.Element("add")
    for obj in hscode.objects.all():
        doc = ET.SubElement(root, "doc")
        ET.SubElement(doc, "field", name="section").text = obj.article.chapter.section.name
        ET.SubElement(doc, "field", name="chapter").text = obj.article.chapter.name
        ET.SubElement(doc, "field", name="article").text = obj.article.heading
        ET.SubElement(doc, "field", name="hs").text = obj.hs
        ET.SubElement(doc, "field", name="id").text = obj.hs
        ET.SubElement(doc, "field", name="desc").text = obj.desc
        ET.SubElement(doc, "field", name="policy").text = obj.policy
        ET.SubElement(doc, "field", name="hs5").text = obj.hs_5
        ET.SubElement(doc, "field", name="hs6").text = obj.hs_6
        ET.SubElement(doc, "field", name="hs8").text = obj.hs_8
        ET.SubElement(doc, "field", name="condition").text = obj.condition

    tree = ET.ElementTree(root)
    tree.write("filename.xml")

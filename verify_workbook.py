import zipfile
import xml.etree.ElementTree as ET

zf = zipfile.ZipFile('IncuBrix_2027_Growth_Engineer_Option_2_Social_Media_and_Content_Submission_Workbook.xlsx')
s1_xml = zf.read('xl/worksheets/sheet1.xml')
s5_xml = zf.read('xl/worksheets/sheet5.xml')

s1 = ET.fromstring(s1_xml)
s5 = ET.fromstring(s5_xml)

print('=== 00_START Target Cells ===')
for cell in ['B5', 'B6', 'B7', 'B11', 'B21', 'B24', 'F5']:
    c = s1.find(f'.//{{*}}c[@r="{cell}"]')
    val = ''.join(c.itertext()) if c is not None else 'None'
    print(cell, val)

print('=== 04_SELF_CHECK Target Cells ===')
for cell in ['C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C29']:
    c = s5.find(f'.//{{*}}c[@r="{cell}"]')
    val = ''.join(c.itertext()) if c is not None else 'None'
    print(cell, val)

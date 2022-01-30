import xml.etree.ElementTree as ET
import os
os.chdir(os.path.join(os.getcwd(), 'Temp'))
tree = ET.parse('contractProcedure_3710603877621000003_164472931.xml')
root = tree.getroot()
subroot = '{http://zakupki.gov.ru/oos/export/1}contractProcedure'
isEDIBased = '{http://zakupki.gov.ru/oos/types/1}isEDIBased'
for child in root.findall(subroot + '/' + isEDIBased):
    print('ok')
    print(child.text)
# for child in root[0]:
#     print(child.tag)

# print(root.tag, root.attrib)
# print(root.find('ns2:export'))
#
# elemList = []
# for el in tree.iter():
#     elemList.append(el.tag)
# print(elemList)

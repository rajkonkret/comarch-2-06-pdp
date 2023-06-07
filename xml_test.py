from xml.dom import minidom

DOMTree = minidom.parse('dane_xml.xml')
print(DOMTree.toxml())

cNodes = DOMTree.childNodes
print(cNodes)
print(cNodes[0])
print(cNodes[0].getElementsByTagName('osoba')[0])
print(cNodes[0].getElementsByTagName('osoba')[1])
print(cNodes[0].getElementsByTagName('osoba')[1].toxml())

print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie'))
print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie')[0].toxml())
# <imie foo="aaaa">Janina</imie>

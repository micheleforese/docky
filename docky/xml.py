from xml.dom import minidom
from docky.console import console

p1 = minidom.parseString('<myxml>Using<empty/> parseString</myxml>')
console.print(p1)

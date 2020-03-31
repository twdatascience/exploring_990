import pandas as pd
import re
import xml.etree.ElementTree as ET

tree = ET.parse('data_0.xml')
root = tree.getroot()

for node in root.iter():
    for elem in node:
        elem.tag = re.sub("{.*}", '', elem.tag)
        print(node.tag, elem.tag, elem.text)

form_dict = {}

sep = ':'

for parent in root:
    if len(parent):
        for child in parent:
            if not len(child):
                new_key = parent.tag + sep + child.tag
                form_dict[new_key] = child.text
            else:
                for sub_child in child:
                    if not len(sub_child):
                        new_key = parent.tag + sep + child.tag + sep + sub_child.tag
                        form_dict[new_key] = sub_child.text
                    else:
                        for sub_child2 in sub_child:
                            if not len(sub_child2):
                                new_key = parent.tag + sep + child.tag + sep + sub_child.tag + sep + sub_child2.tag
                                form_dict[new_key] = sub_child2.text
                            else:
                                for sub_child3 in sub_child2:
                                    if not len(sub_child3):
                                        new_key = parent.tag + sep + child.tag + sep + sub_child.tag + sep + sub_child2.tag + sep + sub_child3.tag
                                        form_dict[new_key] = sub_child3.text
                                    else:
                                        raise ValueError("XML deeper than for loop")

df = pd.DataFrame(form_dict, index=[0])

df.to_csv('test.csv')

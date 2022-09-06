Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Dictionary - key value pair - dictionary
d = {"roll":101,"name":"Gaurav","marks":100}
#dictionary - unordered(no indexing) data collection
d
{'roll': 101, 'name': 'Gaurav', 'marks': 100}
d.keys()
dict_keys(['roll', 'name', 'marks'])
d.values()
dict_values([101, 'Gaurav', 100])
d.items()
dict_items([('roll', 101), ('name', 'Gaurav'), ('marks', 100)])
d["contact"] = 9876543210
d
{'roll': 101, 'name': 'Gaurav', 'marks': 100, 'contact': 9876543210}
#key must be unique
d["name"] = "Mansi Rai"
d
{'roll': 101, 'name': 'Mansi Rai', 'marks': 100, 'contact': 9876543210}
d.popitem()
('contact', 9876543210)
#pop - it will remove last key value pair
d
{'roll': 101, 'name': 'Mansi Rai', 'marks': 100}
d.pop('marks')
100
d
{'roll': 101, 'name': 'Mansi Rai'}
del d['roll']
d
{'name': 'Mansi Rai'}
del d
d
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
x = {'roll': 101, 'name': 'Mansi Rai', 'marks': 100}
x['name']
'Mansi Rai'
x.get('name')
'Mansi Rai'

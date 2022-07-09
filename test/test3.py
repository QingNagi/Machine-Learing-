from collections import OrderedDict

favorite_laguages = OrderedDict()

favorite_laguages['jen'] = 'p'
favorite_laguages['sarah'] = 'c'

for name, language, in favorite_laguages.items():
    print(name.title() +"'s favorite language is " + language.title() + ".")
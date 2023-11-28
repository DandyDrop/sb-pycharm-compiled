a = ['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'add_note', 'args', 'name', 'with_traceback']

with open('b.py', 'w') as f:
    for b in a:
        c = """f'""" + b + ' : {e.' + b + "}'"
        f.write(f'    print({c})\n')




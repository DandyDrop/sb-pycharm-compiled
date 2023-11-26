from seleniumbase.fixtures.base_case import BaseCase

sb = BaseCase()


with open('preconfig.py', 'w') as f:
    f.write('''
from seleniumbase.fixtures.base_case import BaseCase
from seleniumbase.undetected import Chrome
from seleniumbase.undetected.webelement import WebElement


sb = BaseCase()
driver: Chrome = sb.driver
sb.driver = driver

''')
    for d in dir(sb):
        if 'wait_' in d and '__' not in d:
            raw_name = 'raw_' + d
            sb_dot = 'sb.' + d
            new_name = 'new_' + d
            f.write(f'''
{raw_name} = {sb_dot}


def {new_name}(*args, **kwargs) -> WebElement:
    return {raw_name}(*args, **kwargs)
    
    
{sb_dot} = {new_name}

# ----------------------------------------------------------------------------------------------------------------------
''')




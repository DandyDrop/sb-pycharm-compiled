import os
import re

from util import execute

FILEPATH = os.path.join(os.getcwd(), 'mycode.py')

with open(FILEPATH) as f:
    execute(re.search(r'# start\n\n\n(.*?)\n\n# end', f.read(), re.DOTALL).group(1))



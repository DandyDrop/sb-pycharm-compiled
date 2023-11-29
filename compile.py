import os
import re


def compile_sb(
        code_path: str,
        util_name: str = 'util'
):
    src_dir = os.path.sep.join(code_path.split(os.path.sep)[:-1])

    util_python_path = src_dir.replace(os.path.sep, '.') + '.' + util_name

    with open(code_path, 'r') as f:
        code = re.search(
            r'# prepare\n\n(.*?)\n# start\n\n\n(.*?)\n\n# end',
            f.read(),
            re.DOTALL
        )

    prepare_code = '\n'.join(
        line.replace(util_name, util_python_path)
        if 'import' in line and util_name in line else line
        for line in code.group(1).split('\n')
    )

    tab = ' ' * 8
    main_code = '\n'.join(tab + line for line in code.group(2).split('\n'))

    code = f'''import seleniumbase
{prepare_code}
if __name__ == '__main__':
    with seleniumbase.SB(uc=True) as sb:
{main_code}
    '''

    with open('compiled.py', 'w') as f:
        f.write(code)


compile_sb(r'src\mycode.py')




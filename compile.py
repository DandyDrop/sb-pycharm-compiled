import io
import os
import re


def compile_sb(
        code_path: str,
        util_name: str = 'util'
):
    split_code_path = code_path.split(os.path.sep)
    above_src_dir = os.path.sep.join(split_code_path[:-2])

    util_python_path = split_code_path[-2] + '.' + util_name

    with open(code_path, 'r') as f:
        code = re.search(
            r'# prepare\n\n(.*?)\n# start\n\n\n(.*?)\n\n# end',
            f.read(),
            re.DOTALL
        )

    prepare_code = io.StringIO()

    seleniumbase_init = 'with seleniumbase.SB(uc=True)'

    for line in code.group(1).split('\n'):
        if 'import' in line and util_name in line:
            prepare_code.write(line.replace(util_name, util_python_path) + '\n')
        elif 'with seleniumbase.SB' in line:
            seleniumbase_init = line.split(':')[0]
        elif line:
            prepare_code.write(line + '\n')

    tab = ' ' * 8
    main_code = '\n'.join(tab + line for line in code.group(2).split('\n'))

    code = f'''import seleniumbase
{prepare_code.getvalue()}
if __name__ == '__main__':
    {seleniumbase_init} as sb:
{main_code}
    '''

    with open(os.path.join(above_src_dir, 'compiled.py'), 'w') as f:
        f.write(code)


def join_path(*paths):
    paths = [path.split(os.path.sep) for path in paths]
    filtered_paths = paths.pop(0)

    for path in paths:
        first_inter = None
        for i, p in enumerate(path[::-1]):
            if p == filtered_paths[-1]:
                if i != 0:
                    first_inter = i
        if first_inter:
            filtered_paths.extend(path[-first_inter:])
        else:
            filtered_paths.extend(path)

    return os.path.sep.join(filtered_paths)


compile_sb(join_path(os.getcwd(), r'src\mycode.py'))


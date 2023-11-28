import os
import io
import re
import importlib
# from types import ModuleType

import traceback


def to_python_path(path):
    return path[:-3].replace(os.path.sep, '.')


def compile_sb(
        code_path: str,
        util_src_dir_path: str
):
    src_dir = os.path.sep.join(code_path.split(os.path.sep)[:-1])

    util_src_dir_python_path = to_python_path(util_src_dir_path)

    util_path = os.path.join(src_dir, util_src_dir_path)
    util_python_path = to_python_path(util_path)

    with open(code_path, 'r') as f:
        code = re.search(
            r'# prepare\n\n(.*?)\n# start\n\n\n(.*?)\n\n# end',
            f.read(),
            re.DOTALL
        )

    prepare_code = io.StringIO()
    util_imports = []
    import_util_module = False
    for line in code.group(1).split('\n'):
        if util_src_dir_python_path in line and 'import' in line:
            if f'import {util_src_dir_python_path}' in line:
                import_util_module = True
            else:
                util_imports.append(line)
        else:
            prepare_code.write(line + '\n')

    with open(util_path) as f:
        util_code = f.read().split('\n')

    i = 0
    for line in util_code:
        if line and 'import' not in line:
            break
        i += 1

    new_code = util_code[i:]

    with open(util_path, 'w') as f:
        f.write('\n'.join(new_code))

    while True:
        try:
            util = importlib.import_module(util_python_path)
            dir_util_filtered = filter(
                lambda x:
                not (x.startswith('__') and x.endswith('__'))
                and any(x in util_import for util_import in util_imports),
                dir(util)
            )
            break
        except Exception:
            del new_code[
                int(re.findall(
                    util_path.replace('\\', r'\\') + r'", line (\w+)',
                    traceback.format_exc()
                )[0]) - 1
            ]
            with open(util_path, 'w') as f:
                f.write('\n'.join(new_code))

    with open(util_path, 'w') as f:
        f.write('\n'.join(util_code))

    imports_from_util = (
            f'\nfrom {util_python_path} import ' + ', '.join(dir_util_filtered)
    ) if list(dir_util_filtered) else ''

    main_code = '\n'.join(' ' * 8 + line for line in code.group(2).split('\n'))

    code = f'''import seleniumbase{imports_from_util}
{prepare_code.getvalue()}
if __name__ == '__main__':
    with seleniumbase.SB(uc=True) as sb:
{main_code}
    '''

    if import_util_module:
        code = f'import {util_python_path} as util\n' + code

    with open('compiled.py', 'w') as f:
        f.write(code)

# import util
#
# vui = vars(util).items()
#
# module_names = [name for name, v in vui if type(v) is ModuleType]

# names = filter(
#     lambda x: not (
#             (type_v := type(x[1])) is ModuleType
#             or (name := x[0]).startswith('__')
#             or name.endswith('__')
#             or print(repr_v := repr(x[1]))
#             or any(mn in repr_v for mn in module_names)
#     ),
#     vui
# )

# for n in names:
#     pass

# for k, v in vui:
#     type_v = type(v)
#     print(type_v)
#     print(str(type_v))


compile_sb(r'src\mycode.py', 'util.py')




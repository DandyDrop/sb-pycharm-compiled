# sb.driver.get('https://google.com')
#
# for r in sb.driver.requests:
#     print(r)
#
# print(sb.use_wire)
# print(sb.undetectable)
#
#
# sb.driver.close()
# sb.driver.quit()
import json
import seleniumbase
# import traceback

with seleniumbase.SB(uc=True) as sb, open('sb_uc_true.json', 'w') as f:
    sb.get('https://google.com')
    json.dump({
        str(k): str(v) for k, v in vars(sb).items()
        # if v is not None
    }, f, indent=4)

with open(r'sb_uc_true.json', 'r') as f:
    data = json.load(f)

# while True:
#     try:
#         import a
#         break
#     except AttributeError:
#         with open('a.py', 'r') as f:
#             code = f.read().split('''sb.setUp()
# sb.get('https://google.com')''')[0]
#         what = traceback.format_exc().split(" 'BaseCase' object has no attribute '")[-1].strip("' \n")
#         if (w := data[what]) not in ['True', 'False', 'None']:
#             w = f"'{w}'"
#         print(w)
#         new_c = f'sb.{what} = {w}\n'
#         with open('a.py', 'w') as f:
#             f.write(code + new_c + '''sb.setUp()
# sb.get('https://google.com')\n\n\n\n\n\n\n''')

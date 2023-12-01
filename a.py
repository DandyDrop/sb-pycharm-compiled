import json

import seleniumbase
from seleniumwire import webdriver

sb = seleniumbase.BaseCase()

sb.undetectable = True
sb.uc_subprocess = True
sb.settings_file = None
sb.device_metrics = None
sb.mobile_emulator = False
sb.dashboard = False
sb.recorder_mode = False
sb._reuse_session = False
sb.browser = 'chrome'
sb.headless = False
sb.locale_code = None
sb.protocol = 'http'
sb.servername = 'localhost'
sb.port = '4444'
sb.proxy_string = None
sb.proxy_bypass_list = None
sb.proxy_pac_url = None
sb.multi_proxy = False
sb.user_agent = None
sb.cap_file = None
sb.cap_string = None
sb.recorder_ext = None
sb.disable_js = False
sb.disable_csp = False
sb.enable_ws = True
sb.enable_sync = None
sb.use_auto_ext = False
sb.uc_cdp_events = False
sb.log_cdp_events = False
sb.no_sandbox = None
sb.disable_gpu = None
sb.headless2 = False
sb.incognito = False
sb.guest_mode = False
sb.dark_mode = False
sb.devtools = False
sb.remote_debug = False
sb.enable_3d_apis = False
sb.ad_block_on = False
sb.host_resolver_rules = None
sb.block_images = False
sb.do_not_track = False
sb.chromium_arg = None
sb.firefox_arg = None
sb.firefox_pref = None
sb.user_data_dir = None
sb.extension_zip = None
sb.extension_dir = None
sb.binary_location = None
sb.driver_version = None
sb.page_load_strategy = None
sb.use_wire = False
sb.external_pdf = False
sb.xvfb = False
sb.start_page = None
sb.time_limit = None
sb.demo_mode = False

sb.setUp()

sb.driver.close()
sb.driver.quit()

sb.driver = webdriver.Chrome()

sb.driver.get('https://google.com')

with open('sb_bc.json', 'w') as f:
    json.dump({str(k): str(v) for k, v in vars(sb).items()}, f, indent=4)


print(sb.driver.requests)


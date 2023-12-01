import seleniumbase
from seleniumbase.fixtures.base_case import BaseCase
from seleniumbase.undetected import Chrome
from seleniumbase.undetected.webelement import WebElement


if __name__ == '__main__':
    import sys
    import subprocess

    for c in [
        r'python ..\compile.py',
        # r'python ..\compiled.py'
    ]:
        subprocess.run(c.split(' '), capture_output=True)

    sys.exit(0)


sb = BaseCase()
driver: Chrome = sb.driver
sb.driver = driver

raw_wait_for_and_accept_alert = sb.wait_for_and_accept_alert


def new_wait_for_and_accept_alert(*args, **kwargs) -> WebElement:
    return raw_wait_for_and_accept_alert(*args, **kwargs)


sb.wait_for_and_accept_alert = new_wait_for_and_accept_alert

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_and_dismiss_alert = sb.wait_for_and_dismiss_alert


def new_wait_for_and_dismiss_alert(*args, **kwargs) -> WebElement:
    return raw_wait_for_and_dismiss_alert(*args, **kwargs)


sb.wait_for_and_dismiss_alert = new_wait_for_and_dismiss_alert

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_and_switch_to_alert = sb.wait_for_and_switch_to_alert


def new_wait_for_and_switch_to_alert(*args, **kwargs) -> WebElement:
    return raw_wait_for_and_switch_to_alert(*args, **kwargs)


sb.wait_for_and_switch_to_alert = new_wait_for_and_switch_to_alert

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_angularjs = sb.wait_for_angularjs


def new_wait_for_angularjs(*args, **kwargs) -> WebElement:
    return raw_wait_for_angularjs(*args, **kwargs)


sb.wait_for_angularjs = new_wait_for_angularjs

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_attribute = sb.wait_for_attribute


def new_wait_for_attribute(*args, **kwargs) -> WebElement:
    return raw_wait_for_attribute(*args, **kwargs)


sb.wait_for_attribute = new_wait_for_attribute

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_attribute_not_present = sb.wait_for_attribute_not_present


def new_wait_for_attribute_not_present(*args, **kwargs) -> WebElement:
    return raw_wait_for_attribute_not_present(*args, **kwargs)


sb.wait_for_attribute_not_present = new_wait_for_attribute_not_present

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_element = sb.wait_for_element


def new_wait_for_element(*args, **kwargs) -> WebElement:
    return raw_wait_for_element(*args, **kwargs)


sb.wait_for_element = new_wait_for_element

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_element_absent = sb.wait_for_element_absent


def new_wait_for_element_absent(*args, **kwargs) -> WebElement:
    return raw_wait_for_element_absent(*args, **kwargs)


sb.wait_for_element_absent = new_wait_for_element_absent

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_element_clickable = sb.wait_for_element_clickable


def new_wait_for_element_clickable(*args, **kwargs) -> WebElement:
    return raw_wait_for_element_clickable(*args, **kwargs)


sb.wait_for_element_clickable = new_wait_for_element_clickable

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_element_not_present = sb.wait_for_element_not_present


def new_wait_for_element_not_present(*args, **kwargs) -> WebElement:
    return raw_wait_for_element_not_present(*args, **kwargs)


sb.wait_for_element_not_present = new_wait_for_element_not_present

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_element_not_visible = sb.wait_for_element_not_visible


def new_wait_for_element_not_visible(*args, **kwargs) -> WebElement:
    return raw_wait_for_element_not_visible(*args, **kwargs)


sb.wait_for_element_not_visible = new_wait_for_element_not_visible

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_element_present = sb.wait_for_element_present


def new_wait_for_element_present(*args, **kwargs) -> WebElement:
    return raw_wait_for_element_present(*args, **kwargs)


sb.wait_for_element_present = new_wait_for_element_present

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_element_visible = sb.wait_for_element_visible


def new_wait_for_element_visible(*args, **kwargs) -> WebElement:
    return raw_wait_for_element_visible(*args, **kwargs)


sb.wait_for_element_visible = new_wait_for_element_visible

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_exact_text = sb.wait_for_exact_text


def new_wait_for_exact_text(*args, **kwargs) -> WebElement:
    return raw_wait_for_exact_text(*args, **kwargs)


sb.wait_for_exact_text = new_wait_for_exact_text

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_exact_text_not_visible = sb.wait_for_exact_text_not_visible


def new_wait_for_exact_text_not_visible(*args, **kwargs) -> WebElement:
    return raw_wait_for_exact_text_not_visible(*args, **kwargs)


sb.wait_for_exact_text_not_visible = new_wait_for_exact_text_not_visible

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_exact_text_visible = sb.wait_for_exact_text_visible


def new_wait_for_exact_text_visible(*args, **kwargs) -> WebElement:
    return raw_wait_for_exact_text_visible(*args, **kwargs)


sb.wait_for_exact_text_visible = new_wait_for_exact_text_visible

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_link_text = sb.wait_for_link_text


def new_wait_for_link_text(*args, **kwargs) -> WebElement:
    return raw_wait_for_link_text(*args, **kwargs)


sb.wait_for_link_text = new_wait_for_link_text

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_link_text_present = sb.wait_for_link_text_present


def new_wait_for_link_text_present(*args, **kwargs) -> WebElement:
    return raw_wait_for_link_text_present(*args, **kwargs)


sb.wait_for_link_text_present = new_wait_for_link_text_present

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_link_text_visible = sb.wait_for_link_text_visible


def new_wait_for_link_text_visible(*args, **kwargs) -> WebElement:
    return raw_wait_for_link_text_visible(*args, **kwargs)


sb.wait_for_link_text_visible = new_wait_for_link_text_visible

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_non_empty_text = sb.wait_for_non_empty_text


def new_wait_for_non_empty_text(*args, **kwargs) -> WebElement:
    return raw_wait_for_non_empty_text(*args, **kwargs)


sb.wait_for_non_empty_text = new_wait_for_non_empty_text

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_non_empty_text_visible = sb.wait_for_non_empty_text_visible


def new_wait_for_non_empty_text_visible(*args, **kwargs) -> WebElement:
    return raw_wait_for_non_empty_text_visible(*args, **kwargs)


sb.wait_for_non_empty_text_visible = new_wait_for_non_empty_text_visible

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_partial_link_text = sb.wait_for_partial_link_text


def new_wait_for_partial_link_text(*args, **kwargs) -> WebElement:
    return raw_wait_for_partial_link_text(*args, **kwargs)


sb.wait_for_partial_link_text = new_wait_for_partial_link_text

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_partial_link_text_present = sb.wait_for_partial_link_text_present


def new_wait_for_partial_link_text_present(*args, **kwargs) -> WebElement:
    return raw_wait_for_partial_link_text_present(*args, **kwargs)


sb.wait_for_partial_link_text_present = new_wait_for_partial_link_text_present

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_query_selector = sb.wait_for_query_selector


def new_wait_for_query_selector(*args, **kwargs) -> WebElement:
    return raw_wait_for_query_selector(*args, **kwargs)


sb.wait_for_query_selector = new_wait_for_query_selector

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_ready_state_complete = sb.wait_for_ready_state_complete


def new_wait_for_ready_state_complete(*args, **kwargs) -> WebElement:
    return raw_wait_for_ready_state_complete(*args, **kwargs)


sb.wait_for_ready_state_complete = new_wait_for_ready_state_complete

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_text = sb.wait_for_text


def new_wait_for_text(*args, **kwargs) -> WebElement:
    return raw_wait_for_text(*args, **kwargs)


sb.wait_for_text = new_wait_for_text

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_text_not_visible = sb.wait_for_text_not_visible


def new_wait_for_text_not_visible(*args, **kwargs) -> WebElement:
    return raw_wait_for_text_not_visible(*args, **kwargs)


sb.wait_for_text_not_visible = new_wait_for_text_not_visible

# ----------------------------------------------------------------------------------------------------------------------

raw_wait_for_text_visible = sb.wait_for_text_visible


def new_wait_for_text_visible(*args, **kwargs) -> WebElement:
    return raw_wait_for_text_visible(*args, **kwargs)


sb.wait_for_text_visible = new_wait_for_text_visible

# ----------------------------------------------------------------------------------------------------------------------

# prepare

with seleniumbase.SB(uc=True, wire=True, use_wire=True): ...


# start


...


# end





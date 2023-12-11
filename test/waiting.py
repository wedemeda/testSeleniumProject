from time import sleep


def waiting_css_property(web_element, style, expect_value, time):
    while time:
        if expect_value == web_element.value_of_css_property(style):
            break
        sleep(1)
        time = time - 1

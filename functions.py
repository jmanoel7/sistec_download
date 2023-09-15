# -*- coding: utf-8 -*-


from time import sleep

import pyautogui as pg


def clear_downloads(m_browser, m_time_out):
    sleep(m_time_out)
    main_window = m_browser.current_window_handle
    m_browser.switch_to.new_window('tab')
    m_browser.get('about:downloads')
    max_x, max_y = pg.size()
    pg.click(x=max_x/2.0, y=max_y/2.0, duration=1.0, button='right')
    sleep(1.0)
    pg.press('C')
    sleep(m_time_out)
    m_browser.close()
    m_browser.switch_to.window(main_window)
    return None


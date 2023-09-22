# -*- coding: utf-8 -*-

from time import sleep

def clear_downloads(m_browser, m_time_out):
    sleep(m_time_out)
    main_window = m_browser.current_window_handle
    m_browser.switch_to.new_window('tab')
    m_browser.get('chrome://downloads')
    sleep(m_time_out)
    m_browser.close()
    m_browser.switch_to.window(main_window)
    return None

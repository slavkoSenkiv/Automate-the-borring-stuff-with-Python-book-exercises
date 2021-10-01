from selenium import webdriver


def launch_browser(link):
    browser.get(link)


path_to_webdriver = '/Users/ysenkiv/Code/chromedriver'
browser = webdriver.Chrome(executable_path=path_to_webdriver)
browser.maximize_window()
browser.get('https://www.google.com/webhp?hl=uk&sa=X&sqi=2&pjf=1&ved=0ahUKEwj_kufAxqfzAhXRR_EDHekEA5wQPAgI')
url = 'https://www.google.com/webhp?hl=uk&sa=X&sqi=2&pjf=1&ved=0ahUKEwj_kufAxqfzAhXRR_EDHekEA5wQPAgI'

launch_browser(url)
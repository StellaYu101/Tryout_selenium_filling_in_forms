from selenium import webdriver

##open the window with data you want in it
driver = webdriver.Chrome(executable_path=r'C:\Users\Stella Y\Desktop\chromedriver.exe')
url = 'https://n5iu4pwcrb.execute-api.us-east-2.amazonaws.com/schools/search/?district=Kansas'
#driver.maximize_window()
driver.get(url)

##identifying an element (in this case I want a list of school dists)
element = driver.find_element_by_name('district')

##filling in forms
#all_options = element.find_elements_by_tag_name('option')
#for option in all_options:
#	print ('value is: %s' % option.get_attribute('value'))
#	option.click()

##if you only want one option:
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('district'))
select.select_by_value('COLUMBIA 93')

##submit the request
#The button has the value "Search" :) (we can only find by name, tag name, id, etc)
#(in the case above)
#driver.find_element_by_id("submit").click()
element.submit() #in our case, webdriver has submit metho on every element.
##it will go thru until it finds the enclosing form and calls submit.


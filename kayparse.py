from selenium import webdriver
import time
import smtplib

sender = "8guys1block@gmail.com"
receiver = ["dev777@hotmail.com"]
server = smtplib.SMTP('smtp.gmail.com:587')
password = 'fifa2013'
server.ehlo()
server.starttls()
server.login(sender, password)


destinations = ['SFO', 'SJU', 'MIA', 'BCN', 'FRA', 'LIM', 'LHR', 'CUN', 'SJD']
f = open('prices', 'a')

while(True):
	for i in destinations:
		lst = []
		lst_ints = []
		lst_prices = []
		driver = webdriver.Chrome('/Users/devvret/Downloads/chromedriver')
		driver.get('http://www.kayak.com/s/search/air?d1=01/09/14&depart_flex=3&d2=01/19/14&return_flex=3&l1=BOS&l2='+ i)
		time.sleep(25)
		try:
			#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bestPrice")))
			element = driver.find_elements_by_class_name("bestPrice")
			#print element
			#source = element.get_attribute("innerHTML")
			#print source
			for x in element:
				source = x.get_attribute("innerHTML")
				lst.append(source)
		finally:
			driver.quit()

		for x in lst:
			y = x[1:]
			try:
				z = int(y)
				lst_ints.append(z)
			except:
				pass

		lst_ints.sort()
		print lst_ints
		best_price = lst_ints[0]
		best_price_string = str(best_price)
		f.write("best price for " + i + "is ")
		f.write(best_price_string + '\n')
		if(best_price < 300):
			message = "Flight avaliable to " + i + " for " + best_price_string
			server.sendmail(sender, receiver, message)
		time.sleep(10)

f.close()
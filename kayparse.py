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

depart_dates = ['12/26/13', '01/04/14', '1/09/14', '01/14/14']
arrival_dates = ['01/02/14', '01/11/14', '01/17/14', '01/23/14']
dates = zip(depart_dates, arrival_dates)
departure = ['SFO', 'OAK', 'BOS']
destinations = ['HNL', 'SJU', 'BCN', 'FRA', 'LIM', 'LHR', 'CUN', 'SJD']
f = open('prices', 'a')

while(True):
	for a,b in dates:
		for d in departure:
			for i in destinations:
				lst = []
				lst_ints = []
				lst_prices = []
				driver = webdriver.Chrome('/Users/devvret/Downloads/chromedriver')
				driver.get('http://www.kayak.com/s/search/air?d1=' +a+'&depart_flex=3&d2=' +b+'&return_flex=3&l1='+ d+'&l2='+ i)
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
				print d + " " + i + "from " a + "to " + b, lst_ints
				best_price = lst_ints[0]
				best_price_string = str(best_price)
				f.write("best price for " + i + "departing from " + d + "on " + a + "and arriving " + b + "is ")
				f.write(best_price_string + '\n')
				if(best_price < 300):
					message = "Flight avaliable to " + i + " for " + best_price_string + "departing from " + d
					server.sendmail(sender, receiver, message)
				time.sleep(10)

f.close()
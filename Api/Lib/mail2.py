import  requests
#https://app.mailgun.com/app/account/setup

api=""
apikey=""
from_person=""
def send_simple_message(address,title,content):
	""" mail gönderen fonksiyon  """
	return requests.post(
		api,
		auth=("api", apikey),
		data={"from": from_person,
			"to": address,
			"subject": title,
			"text": content})



""" kullanım örneği """
#send_simple_message("sea-97@hotmail.com","deneme123","denedeneme")

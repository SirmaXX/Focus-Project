import  requests
#https://app.mailgun.com/app/account/setup

api="https://api.mailgun.net/v3/sandbox299fa714339d46b3aee883306af4f6f7.mailgun.org/messages"
apikey="d7f587845eb726eee0ca0777a6c4778e-78651cec-1e7d3ca4"
from_person="Admin <admin@gmail.com>"
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

import requests
import os

GOTIFY_URL = os.environ.get('GOTIFY_URL')
GOTIFY_APP_ID = os.environ.get('GOTIFY_APP_ID')
GOTIFY_KEY = os.environ.get('GOTIFY_KEY')
OUTPUT_PATH = "./output/"

def getMessages():
  url = GOTIFY_URL+"/application/"+GOTIFY_APP_ID+"/message"

  payload={}
  headers = {
    'X-Gotify-Key': GOTIFY_KEY
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  return response.json().get('messages')

def filterValidMessages(messages):
  valid_messages = []
  for message in messages:
    text = message.get('message')
    if text.startswith('-----BEGIN PGP MESSAGE-----'):
      valid_messages.append(message)
  return valid_messages

def writeMessagesToFile(messages):
  for message in messages:
    with open(OUTPUT_PATH+str(message.get('id'))+'.gpg', 'a') as f:
      f.write(message.get('message'))

def deleteMessages(messages):
  for message in messages:
    url = GOTIFY_URL+"/message/"+str(message.get('id'))
    payload={}
    headers = {
      'X-Gotify-Key': GOTIFY_KEY
    }

    requests.request("DELETE", url, headers=headers, data=payload)

def main():
  messages = getMessages()
  valid_messages = filterValidMessages(messages)
  writeMessagesToFile(valid_messages)
  deleteMessages(valid_messages)


if __name__ == "__main__":
    main()

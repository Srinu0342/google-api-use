from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
import winsound

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/','https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels',[])
    # Call the Gmail API to fetch INBOX
    label=[]
    if not labels:
        print('No labels found.')
    else:
        c=0
        for i in labels:
            label.append(i['name'])
            print('index: '+str(c)+' label: '+i['name'])
            c=c+1


    a=int(input('enter label number: '))

    results1 = service.users().messages().list(userId='me',labelIds = [label[a]]).execute()
    messages = results1.get('messages', [])
    i=0
    for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print('id: '+msg['id'])
            for j in msg['payload']['headers']:
                if j['name'] in ['From','Subject']:
                    print('payload: '+str(j))
            try:
              service.users().messages().delete(userId='me', id=message['id']).execute()
              #print(i)
              i=i+1
            except error:
              print('An error occurred: %s' % error)

    return i

def DeleteMessage(service, user_id, msg_id):
  try:
    service.users().messages().delete(userId=user_id, id=msg_id).execute()
    print('Message with id: %s deleted successfully.' % msg_id)
  except error:
    print('An error occurred: %s' % error)

if __name__ == '__main__':
    x=main()
    print(x)
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

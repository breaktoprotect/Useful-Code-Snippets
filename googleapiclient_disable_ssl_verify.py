# Credit: https://medium.com/@butteredwaffles 
# Original code found from: https://medium.com/@butteredwaffles/working-with-google-calendar-api-8121d5048597

from googleapiclient.discovery import build
from oauth2client import file, client, tools
from datetime import datetime
import httplib2

# To disable TLS/SSL for testing (security warning! This will temporarily remove the capability of TLS/SSL transport security enforcement)
my_http = httplib2.Http(disable_ssl_certificate_validation=True)
#my_http = httplib2.Http(ca_certs='./burp.pem') # For self-signed cert, uncomment, and comment the line before this.

SCOPES = "https://www.googleapis.com/auth/calendar.readonly"
store = file.Storage('token.json')
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store, http=my_http)

    service = build('calendar', 'v3', http=creds.authorize(my_http))

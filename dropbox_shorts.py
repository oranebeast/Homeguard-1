# Include the Dropbox SDK
import dropbox

####################################

# DO NOT TOUCH THESE EVER!!!!
app_key = '7kqv2t692l369j9'
app_secret = '5tvt2wdqti3m7op'

####################################

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()
client = dropbox.client.DropboxClient(access_token)
print 'Linked account: ', client.account_info()
print 'Is the linked account correct?, Input YES or NO'
awnser=input()
if awnser = 'YES' :
  print 'Authorized'
if awnser = 'NO' :
  print 'Restarting authorization process'
  flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
  authorize_url = flow.start()
  print '1. Go to: ' + authorize_url
  print '2. Click "Allow" (you might have to log in first)'
  print '3. Copy the authorization code.'
  code = raw_input("Enter the authorization code here: ").strip()
  client = dropbox.client.DropboxClient(access_token)
  print 'Linked account: ', client.account_info()
  print 'Is the linked account correct?, Input YES or NO'
  awnser=input()
  if awnser = 'NO' :
    'Restart the application and try again, Also make sure you have a connection to the internet"


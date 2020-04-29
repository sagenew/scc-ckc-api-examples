import urllib.parse, urllib.request, json, ssl

# Authentication and API Requests

# LEARNING LAB 2  Cisco Kinetic for Cities
# The Initial login steps are the same as Learning Lab 1.
# You can skip ahead to 'LEARNING LAB 2 CODE BEGINS HERE'

#Ignore invalid Certificates
ssl._create_default_https_context = ssl._create_unverified_context


############################### LEARNING LAB 2 CODE BEGINS HERE ############################
#
# In this example, we will exercise the CKC API: {{Platform Instance URL}}/cdp/v1/locations/user/{userId}/info
# In the case of the Sandbox lab, this resolves to https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/locations/user/{userId}/info
# The access_token and user_id from Learning Lab 1 will be used to obtain the current Users Location Information

print('Learning Lab 2 Starts Here:')
user_id = '86847897-ab35-489c-af17-6fbf301a6016'
access_token = '0f493c98-9689-37c4-ad76-b957020d0d6c'

#Define the required GET Headers needed by the CKC API
headers = {
    'authorization': "Bearer " + access_token,
    'Content-Type': "application/json"
    }

#The URL with queryParms to request user details
requestUrl = 'https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/locations/user/' + user_id + '/info'

print('\nGetting User Location Info: (' + requestUrl + ')\n')

# create the request
request = urllib.request.Request(requestUrl, headers = headers)

# perform the request
response = urllib.request.urlopen(request)

results = response.read().decode(encoding)
responseDictionary = json.loads(results)

print('User Location Info:', results, '\n')

############################### LEARNING LAB 2  PART-2 ############################
#
# In this example, we will exercise the CKC API: {{Platform Instance URL}}/cdp/v1/capabilities/customer
# In the case of the Sandbox lab, this resolves to https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/capabilities/customer
# The access_token obtained as explained in Learning Lab 1 is used for authorization

#Define the required GET Headers needed by the CKC API
headers = {'authorization': "Bearer " + access_token }

#The URL with queryParms to request user details
requestUrl = 'https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/capabilities/customer'

print('\nGetting User capabilities: (' + requestUrl + ')\n')

# create the request
request = urllib.request.Request(requestUrl, headers = headers)

# perform the request
response = urllib.request.urlopen(request)

results = response.read().decode(encoding)
responseDictionary = json.loads(results)

print('User Capabilities:', results, '\n')

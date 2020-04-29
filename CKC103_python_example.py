import urllib.parse, urllib.request, json, ssl, xmltodict

# Authentication and API Requests
# LEARNING LAB 3  Cisco Kinetic for Cities
# The Initial login steps are the same as Learning Lab 1.
# You can skip ahead to 'LEARNING LAB 3 CODE BEGINS HERE'
# Note that you may need to manually install matplotlib and xmltodict
# To do this, open a CMD/terminal window and enter 'PIP INSTALL matplotlib' and 'PIP INSTALL xmltodict'


#Ignore invalid Certificates
ssl._create_default_https_context = ssl._create_unverified_context

#   1) Logging In
# The CKC URL needed for initial login
loginUrl = 'https://ckcsandbox.cisco.com/corev4/token'
encoding = 'UTF-8'

access_token = 'db5ec3bb-9bc1-3fde-b6fc-701ef1884e2f'
print("Learning Lab 3 Starts Here:")

#This is the URL we use to get ligting data
requestUrl = "https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/devices"

# create the TQL POST Body
postData = {  
	"Query": {
	    "Find": {
	        "Light" : {
	            "sid": {
	                "ne": ""
	            }
	        }
	    }
	}
}

data = urllib.parse.urlencode(postData)   # urlencode the data
binary_data = data.encode(encoding)  # POST needs binary data, so encode it
# urlopen with data causes a POST request instead of a GET
request = urllib.request.Request(requestUrl, data=binary_data)
request.add_header('authorization', "Bearer " + access_token)
#request.add_header('Content-Type', "application/json")

print("\nRequesting Real Time Lighting Data: (" + requestUrl + ")\n")

# perform the request
response = urllib.request.urlopen(request)

#The results are received as XML
results = response.read().decode(encoding)

# If the data were formatted as json, the line below would create a dictionary from it.
#responseDictionary = json.loads(results)


#Convert the XML data to a Dictionary
responseDictionary = xmltodict.parse(results)

print(responseDictionary)


# Here we're going to draw a pie chart based on the %on/%off of the lights in the database
import matplotlib.pyplot as plt

# specify some colors
colors = ['yellowgreen', 'lightcoral']
# create the labels
labels = ['On', 'Off']
values = [0, 0]

if 'Find' in responseDictionary:
    findObject = responseDictionary['Find']
    if 'Result' in findObject:
        results = findObject['Result']

    for r in results:
        if 'Light' in r:
            light = r['Light']

            # we now have an instance of a CKC Platform light model
            # get the 'state' object
            # this contains 'intensityLevel', 'powerConsumption' and 'reliability'
            if light['state']:
                state = light['state']
                print('state', state)
            if state['intensityLevel']:
                intensityLevel = state['intensityLevel']
            if intensityLevel['request']:
                theRequest = intensityLevel['request']
            if theRequest['value']:
                value = theRequest['value']
            if float(value) > 0:
                # light is on
                values[0] = values[0] + 1
            else:
                # light is off
                values[1] = values[1] + 1


plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=True)

# make the graph a circle (not setting this can result an an elipsis)
plt.axis('equal')

# set the title of the plot and add some additional information - the total number of lights
plt.title('Current Lighting States (Total Lights '+ str(values[0] + values[1]) + ')')

# show the graph
plt.show()

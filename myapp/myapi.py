from myapp import app

from flask import request

# get api/routes?driverid=23

# or

# get api/routes/23

# return all routes for driver id provided

@app.route('/api/routes/')
def get_routes_for_driver():

    driverid = request.args.get('driverid')
    # todo check if valid ..
    return 'this is an api call for driver id ' + str(driverid)

# Driver has arrived at site

#  put to an url with updated data
# paramters will be time, site ...


# For testing

# curl -X PUT --data "siteid=3" 127.0.0.1:5000/api/destination/arrived
# returns 'this is an api call for site 3'

@app.route('/api/destination/arrived', methods=['PUT'])
def arrived_at_destination():
    site = request.form['siteid']
    driverid = request.form['driverid']
    return 'this is an api call for site ' + str(site)   + ' ' + driverid + '\n'
    # todo return JSON response


# Driver has arrived at pickup site

#  put to an url with updated data
# paramters will be time, site ...

@app.route('/api/pickup/arrived')
def made_pickup():
    siteid= request.form['siteid']
    return 'this is an api call for site id ' + str(siteid)



@app.route('/api')
def apicall():
    return 'this is an api call'


## On the Android side of things
# Make get, post, put ... requests to this server
# https://developer.android.com/training/volley/simple.html
# convert JSON to Java objects, preferably with GSON

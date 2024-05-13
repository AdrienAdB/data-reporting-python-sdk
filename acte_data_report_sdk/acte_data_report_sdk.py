import requests


class ReportApi():

    ##
    # initialize class with api base_url
    ##
    def __init__(self, _base_url):

        self.base_url = _base_url
        self.token = None
        self.is_connected = False

    ##
    # connect to reporting api
    ##
    def connect(self, _username, _password):

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        params = { "username": _username, "password": _password }

        self.token = None

        try:
            response = requests.post(self.base_url +"/api/token", headers=headers, data=params)
            data = response.json()
            self.token = data['access_token']
            self.is_connected = True
        except Exception as e:
            self.is_connected = False
            print(response.text)
            raise Exception(e)

    ##
    # check token
    ##
    def check_connection(self):
        if not self.token:
            raise Exception("No token found, please connect first")

        if self.is_connected:
            return True
        else:
            raise Exception("Not connected. please connect first")


    ##
    # get user allowed databases (list)
    ##
    def getDatabases(self):

        self.check_connection()
        headers = { 'Authorization': 'Bearer '+ self.token }

        try:
            response = requests.get(self.base_url +"/api/users/me", headers=headers)
            data = response.json()
            databases = data['databases']
            if(len(databases) == 0):
                raise Exception("No authorized databases found, please contact your administrator to grant access")

            return databases

        except Exception as e:
            raise Exception(e)

    ##
    # get devices list (list)
    # params:
    #    db: string
    ##
    def getDevices(self, db):

        self.check_connection()
        headers = { 'Authorization': 'Bearer '+ self.token }

        try:
            url = self.base_url +"/api/v3/%s/devices" % (db)
            response = requests.get(url, headers=headers)

            if not response.ok:
                raise Exception(response.text)

            devices = response.json()
            return devices

        except Exception as e:
            print(response.text)
            raise Exception(e)

    ##
    # get keys (list)
    # params:
    #    db: string
    #    device: device
    ##
    def getKeys(self, db, device):

        self.check_connection()
        headers = { 'Authorization': 'Bearer '+ self.token }
        params = {"device": device}

        try:
            url = self.base_url +"/api/v3/%s/keys" % (db)
            response = requests.get(url, headers=headers, params=params)

            if not response.ok:
                raise Exception(response.text)

            keys = response.json()
            return keys

        except Exception as e:
            print(response.text)
            raise Exception(e)


    ##
    # get telemtery (list)
    # params:
    #    db: string
    #    device: string
    #    key: string
    #    from_date: timestamp
    #    to_date: timestamp
    #
    ##
    def getTelemetry(self, db, device, key, from_date, to_date, agg_interval = None, agg_type = None):

        self.check_connection()
        headers = { 'Authorization': 'Bearer '+ self.token }
        params = {
            "device": device,
            "key": key,
            "from_date": round(from_date),
            "to_date": round(to_date)
        }

        if agg_interval:
            params['agg_interval'] = int(agg_interval)
        if agg_type:
            params['agg_type'] = str(agg_type)

        try:
            url = self.base_url +"/api/v3/%s/telemetry" % (db)
            response = requests.get(url, headers=headers, params=params)

            if not response.ok:
                raise Exception(response.text)

            keys = response.json()
            return keys

        except Exception as e:
            print(response.text)
            raise Exception(e)

# Data Reporting Python SDK

- Collect your data via ACTE Technology secured gateway


## Installation

- install Python3
- git clone https://gitlab.acte.solutions/adrien/data-reporting-python-sdk.git
- pip3 install -r requirements.txt


# Configuration

- Contact ACTE support in order to receive username, password and authorized databases
- copy below code and edit configuration variables

## Example

```python

from data_reporting_python_sdk import report_api
from pprint import pprint
from datetime import datetime, timedelta

# Configuration variables
API_USERNAME = "YOUR_USERNAME"
API_PASSWORD = "YOUR_PASSWORD"
BASE_URL = "https://gw7.acte.ltd"
db = "DATA_DB" # database



# init api class and connect
api = report_api.ReportApi(BASE_URL)
api.connect(API_USERNAME, API_PASSWORD)

# get allowed databases
databases = api.getDatabases()
pprint(databases)

# get devices
devices = api.getDevices(db)
pprint(devices)
device = devices[0] # first device

# get keys
keys = api.getKeys(db, device)
pprint(keys)


# get telemetry data
#    prepare configuration parameters
to_ts = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
from_ts = ( datetime.now() - timedelta(days=7) ).replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
key = keys[0] # first key
agg_type = "SUM" # or "AVG" for average
agg_interval = 3600 # 1day

data = api.getTelemetry(db, device, key, from_ts, to_ts, agg_interval=agg_interval, agg_type=agg_type)
pprint(data)
```

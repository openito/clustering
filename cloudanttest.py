from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
serviceid='ServiceId-660bf6eb-2e16-4edb-9d24-423178fb1dc9'
apikey='CGNgGhFnuf_-7EmJh3z1Y7C0S3H-f-cQzRJ8ZX8ARd-0'
apikey2='Ssa7MlveHnHE-_x6HtdN-s5u_540ijloiRskjOmqxDPA'
client = Cloudant("junzhe.joseph.zhu@gmail.com", "Tianji123!", url="http://opendata.mybluemix.net/crimes?")
client.connect()
databaseName = "crimedata"

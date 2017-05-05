#comparing two api json objects and printing the difference

import requests

#asiging API URLS
dev_server = 'http://dev_server_url/api/'
cloud_server = 'https://cloud_server_url/api/'
p = 'datalake/'

#request api in json
dev_result = requests.get(dev_server+p,auth=('uname','pword'))
data_dev = dev_result.json()

cloud_result = requests.get(cloud_server+p,auth=('uname','pword'))
data_cloud = cloud_result.json()

#declaring list
data_cloud_list = list()
data_dev_list = list()

#fetching keys from dict and putting in list
for key in data_cloud.keys():
  data_cloud_list.append(key)

for key in data_dev.keys():
  data_dev_list.append(key)

#using set for comparing two lists and printing difference
c = set(data_dev_list).union(set(data_cloud_list))
d = set(data_dev_list).intersection(set(data_cloud_list))
list(c - d)

print list
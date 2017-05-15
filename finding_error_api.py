import requests


url = "url/api/dashboard/"

t=requests.get(url,auth=('uname','pwd'))
data = t.json()

list_of_id = list()
list_of_users = list()

for item in data['result']:
    list_of_id.append(item['id'])

print list_of_id


for a in list_of_id:
    open_id = "url/api/dashboard/" + str(a)
    open_id_req = requests.get(open_id,auth=('uname','pwd'))
    open_id_data = open_id_req.json()
    # print open_id_req.json()
    for b in open_id_data['objects']:
        list_of_users.append(b['data'])

print list_of_users


for c in list_of_users:
    open_final = "url" + str(c)
    open_final_req = requests.get(open_final,auth=('uname','pwd'))
    if (open_final_req.ok):
        print "working" + c

    else:
        open_final_req.raise_for_status()


# print data_list
# myResponse.raise_for_status()
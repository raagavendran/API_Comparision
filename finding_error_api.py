import requests
import getpass

host = raw_input('Enter host address: ')
url = host + "/api/dashboard/"
list_of_id = list()
list_of_users = list()

cokkie_session = requests.Session()
uname = raw_input('Enter username: ')
pword =getpass.getpass()
cokkie_session.auth = (uname,pword)
t = cokkie_session.get(url)
print cokkie_session.cookies
dashboard_data = t.json()

for passing_id in dashboard_data['result']:
    list_of_id.append(passing_id['id'])
print "Total number of Custom Dashboard: "+ str(len(list_of_id))
print "List of Custom Dashboard ID: "+str(list_of_id)

for a in list_of_id:

        list_of_users = []
        open_id = url + str(a)
        open_id_req = cokkie_session.get(open_id)
        open_id_data = open_id_req.json()
        print '*'* 100
        print "Checking dashboard: "+ str(open_id_data['name'])
        print '_' * 100
        for b in open_id_data['objects']:
            list_of_users.append(b['data'])
        for c in list_of_users:
            print "Checking :" + c
            try:
                open_final = host + str(c)
                open_final_req = cokkie_session.get(open_final)
                open_final_req.raise_for_status()
                if (open_final_req.ok):
                    print "status OK"
            except requests.HTTPError as err:
                print "status ERROR"

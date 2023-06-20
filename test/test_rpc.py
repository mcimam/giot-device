import xmlrpc.client
url = 'http://localhost:8069'
db = 'kr_v15'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
cmds = models.execute_kw(db, uid, password, 
                         'giot.device.cmd', 
                         'search_read', 
                         [[('device_id.mac', '=', '2123'),('is_success','=',False)]],
                         {'fields': ['method', 'params', 'is_return'], 
                          'limit': 5})

# cmd_id = cmds[0]["id"]
# models.execute_kw(db,uid, password,
#                 'giot.device.cmd', 
#                 'rtr_cmd', 
#                 [cmd_id, {'status':True}]
#                 )

# tests = models.execute_kw(db, uid, password, 
#                          'giot.device.cmd', 
#                          'get_cmd',
#                          [])


                         
print(cmds)
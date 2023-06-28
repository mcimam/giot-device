# Script to directly call xmlrpc
# I am just tired LOL

import xmlrpc.client
from config import RPC_DB, RPC_URL, RPC_PASS, RPC_USER

class OdooAPI:
    def __init__(self, mac) -> None:
        self.url = RPC_URL
        self.db = RPC_DB
        self.user = RPC_USER
        self.passwd = RPC_PASS
        self.mac = mac

        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = common.authenticate(self.db, self.user, self.passwd, {})        
        self.model = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))        
    
    def get_cmd(self):
        cmds = self.model.execute_kw(self.db,self.uid, self.passwd, 
                         'giot.device.cmd', 
                         'search_read', 
                         [[('device_id.mac', '=', self.mac),('is_success','=',False)]],
                         {'fields': ['method', 'params', 'is_return'], 
                          'limit': 5})
        
        return cmds
    
    def rtr_cmd(self, cmd_id, result):
        self.model.execute_kw(self.db,self.uid, self.passwd, 
                    'giot.device.cmd', 
                    'rtr_cmd', 
                    [cmd_id, result]
                    )
                
    def report_log(self, param):
        self.model.execute_kw(self.db,self.uid, self.passwd, 
                         'giot.device.log', 
                         'append_log', [], 
                         {
                            'device_mac': self.mac,
                            'logs': param
                        })
    
    def test(self):
        print('test')
    
    

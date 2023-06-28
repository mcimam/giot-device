# API

You can use one of this backend or even create new one.

## MQTT

Message standar follow basic json rpc but with slight modification.

**Log Message**
``` json
{
    "id": "<random uid>",
    "config": {
        // printout current config
    },
    "device": {
        "dht": 0,
        "water": 0,
        "tds" : 0,
        "relay": 0
    }
}
```

**Command Message**
``` json
// command message
{
    "id": "<random uids>",
    "method": "", //
    "params": {
        // all params need for method
    }
} 

// result message
{
    "id": "<cmd id>",
    "result" : "",
    "error": "",
}
```

## ODOO API
Please refer to (here)[https://github.com/mcimam/giot-odoo/]

This API follow ODOO xml rpc protocol. Here's available method:

**append_log**
```json
{
    "device_mac": "",
    "logs" : {
        "dht": 0,
        "water": 0,
        "tds" : 0,
        "relay": 0,
    }
}
```

**rtr_cmd**
```json
// result message
{
    "id": "<cmd id>",
    "result" : "",
    "error": "",
}
```

from __future__ import print_function

import boto3
import datetime
import json
import time

print('Loading function')

gColdRun = None
def handler(event, context):
    time.sleep(0)
    global gColdRun
    ret = 'hot||%s' % datetime.datetime.now()
    if gColdRun is None:
        gColdRun = True
        ret = 'cold||%s' % datetime.datetime.now()
    print(ret)
    retBody ={
        "statusCode":200,
        "body":ret
    }
    print(retBody)
    return retBody

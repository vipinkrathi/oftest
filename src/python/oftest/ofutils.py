
"""
Utilities for the OpenFlow test framework
"""

import random
import oftest.message as message

def gen_xid():
    return random.randrange(1,0xffffffff)

def of_error_msg_make(type, code, data):
    """ Construct a new ofp_error message
    
    #@todo should probably move into oftest.messages, BUT that's autogenerated code!
    """
    err = message.error()
    err.type = type
    err.code = code
    err.data= data
    return err
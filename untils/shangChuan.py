# -*- coding: utf-8 -*-
# @Date    : 2017-09-16 15:17:38
# @Author  : lileilei
from qiniu import Auth,put_file,etag,urlsafe_base64_encode
import qiniu.config
access_key='uVxowDUcYx641ivtUb111WBEI4112L3D117JHNM_AOtskRh4'
secret_key='PdXU9XrXTLtp1N21bhU1Frm1FDZqE1qhjkEaE9d1xVLZ5C'
def sendfile(key,file):
    q=Auth(access_key,secret_key)
    bucket_name='leilei22'
    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, file)
    me= ret['hash']
    f=etag(file)
    if me==f:
        assert_t=True
    else:
        assert_t=False
    return assert_t

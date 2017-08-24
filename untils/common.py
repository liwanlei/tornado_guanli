# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 13:04:35
# @Author  : lileilei 
import hashlib
from datetime import datetime
def encrypt(key):
	hash=hashlib.md5()
	hash.update(key.encode("utf-8"))
	return hash.hexdigest()
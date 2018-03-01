#coding=utf-8
import get_token

corp_id = 'wx1d422f41ba7a2904'
Secret = 'Ta68AqynGlZiEaVRydONupS9Gd4A7uj2iMb2KONSrjSRd0DB4dwbc3rhP2JL7_VA'
rs_token = get_token.get_token_in_time(corp_id, Secret)
def get_rs_token():
    f = open('get_rs_token.log','w')
    f.write(rs_token)
    f.close()
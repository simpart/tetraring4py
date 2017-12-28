import os, requests, base64, hmac, hashlib, time, wsgiref.handlers
from Define import Define

def send_img(uuid):
    try:
        image = open(os.path.dirname(os.path.abspath(__file__)) + '/../taira.jpg', 'rb')
        uri = "/backend/" + uuid
        headers = {
            'Date': wsgiref.handlers.format_date_time(time.time()),
            'Content-Type': 'multipart/form-data'
        }

        h = hmac.new(
                Define.SUIT_APIKEY,
                'GET\n\n' + headers['Content-Type'] + '\n' + headers['Date'] + '\n' + uri,
                hashlib.sha256
        )
        headers['Authorization'] = Define.SUIT_USER + ':' + base64.encodestring(h.digest()).strip()
        files = {'param_name': ('filename.jpg', image, 'image/jpeg')}
        
        return requests.put(
                   'http://' + Define.SUIT_HOST + ':' + Define.SUIT_PORT + uri,
                   headers=headers,
                   files=files
               )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e


def send(uri):
    try:
        headers = {
            'Date': wsgiref.handlers.format_date_time(time.time()),
            'Content-Type': 'application/json'
        }
        
        h = hmac.new(
                Define.SUIT_APIKEY,
                'GET\n\n' + headers['Content-Type'] + '\n' + headers['Date'] + '\n' + uri,
                hashlib.sha256
        )
        headers['Authorization'] = Define.SUIT_USER + ':' + base64.encodestring(h.digest()).strip()

        # print 'http://' + Define.SUIT_HOST + ':8081' + uri
        return requests.get('http://' + Define.SUIT_HOST + ':' + Define.SUIT_PORT + uri, headers=headers)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e

# end of file

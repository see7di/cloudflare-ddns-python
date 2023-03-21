import urllib
import urllib.request
import urllib.parse
import json

ZONE_ID    = 'f5a5e86ea16a1ab312f43a9624ed7060'  # 这个标识了域名
TOKEN      = '72UYxeU3dgxGnXPjRxCwIckkwGcHUQQtIHkT06cN' # api授权，请按照指示生成
# 请不要给任何人看你的TOKEN，这里的示范已经经过了修改


def get_headers(
        token:str, 
        content_type:str = ''
        ) -> dict:
    d = {}
    d["User-Agent"] = "curl/7.55.1"
    d["Authorization"] = f"Bearer {token}"
    if content_type:
        d["Content-Type"] = content_type
    return d


def get_apis(
        token:str,    
        zone_id:str,
        ):
    def list_records() -> str:
        headers = get_headers(token) 
        req = urllib.request.Request(
            'https://api.cloudflare.com/client/v4/zones/' + zone_id + '/dns_records',
            headers = headers,
            )
        with urllib.request.urlopen(
                req,
                timeout=5
                ) as response:
            html = response.read()
            return html.decode()

    def create_record(
            record_type:str, 
            name:str,
            ip:str
            ) -> str:
        headers = get_headers(
                token,
                "application/json",
                )
        data = {}
        data["type"] = record_type
        data["name"] = name
        data["content"] = ip 
        data["ttl"] = 1
        data["proxied"] = False 
        payload = json.dumps(data).encode()
        req = urllib.request.Request(
            'https://api.cloudflare.com/client/v4/zones/' + zone_id + '/dns_records',
            headers = headers,
            data = payload,
            method='POST'
            )
        with urllib.request.urlopen(
                req,
                timeout=10
                ) as response:
            html = response.read()
            return html.decode()

    def update_record(
            record_id:str,
            record_type:str, 
            name:str,
            ip:str
            ) -> str:
        headers = get_headers(
                token,
                "application/json",
                )
        data = {}
        data["type"] = record_type
        data["name"] = name
        data["content"] = ip 
        data["ttl"] = 1
        data["proxied"] = False 
        payload = json.dumps(data).encode()
        req = urllib.request.Request(
            'https://api.cloudflare.com/client/v4/zones/' + zone_id + '/dns_records/' + record_id,
            headers = headers,
            data = payload,
            method='PUT',
            )
        with urllib.request.urlopen(
                req,
                timeout=10,
                ) as response:
            html = response.read()
            return html.decode()

    def delete_record(
            record_id:str,
            ) -> str:
        headers = get_headers(
                token,
                "application/json",
                )
        req = urllib.request.Request(
            'https://api.cloudflare.com/client/v4/zones/' + zone_id + '/dns_records/' + record_id,
            headers = headers,
            method='DELETE',
            )
        with urllib.request.urlopen(
                req,
                timeout=10,
                ) as response:
            html = response.read()
            return html.decode()

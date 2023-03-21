def get_headers(
        token:str, 
        content_type:str
        ) -> dict:
    d = {}
    d["User-Agent"] = "curl/7.55.1"
    d["Authorization"] = f"Bearer {token}"
    if content_type:
        d["Content-Type"] = "application/json"
    return d


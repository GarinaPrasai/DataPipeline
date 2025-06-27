from pydantic import BaseModel

class Host(BaseModel):
    host_id: str
    hostname: str
    ip_address: str
    os: str
    last_seen: str

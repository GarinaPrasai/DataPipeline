from typing import List, Dict

class DataNormalizer:
    @staticmethod
    def normalize_host(host: dict) -> Dict:
        return {
            "host_id": host.get("host_id", ""),
            "hostname": host.get("hostname", ""),
            "ip_address": host.get("ip_address", ""),
            "os": host.get("os", ""),
            "last_seen": host.get("last_seen", ""),
        }
    
    @staticmethod
    def normalize_hosts(hosts: List[dict]) -> List[Dict]:
        return [DataNormalizer.normalize_host(host) for host in hosts]

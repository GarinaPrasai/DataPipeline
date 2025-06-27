from typing import List, Dict

class DataDeduper:
    @staticmethod
    def dedupe_hosts(hosts: List[Dict]) -> List[Dict]:
        seen = {}
        for host in hosts:
            host_id = host["host_id"]
            if host_id not in seen:
                seen[host_id] = host
            else:
                # Merge hosts with the same ID (e.g., taking the latest data)
                seen[host_id].update(host)
        return list(seen.values())

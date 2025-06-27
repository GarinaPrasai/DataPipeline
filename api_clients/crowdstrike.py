import os
from typing import List

class CrowdstrikeAPIClient:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.test_mode = os.getenv("TEST_MODE", "true").lower() == "true"
        self.base_url = "https://crowdstrikeapi.example.com"  # Placeholder

    def fetch_hosts(self) -> List[dict]:
        if self.test_mode:
            print("[Crowdstrike] 🔁 Using mock data (TEST_MODE=True)")
            return [
                {
                    "host_id": "c-001",
                    "hostname": "crowd-host-1",
                    "ip_address": "10.0.0.5",
                    "os": "macOS",
                    "last_seen": "2023-06-05"
                },
                {
                    "host_id": "q-002",
                    "hostname": "overlap-host",
                    "ip_address": "10.0.0.6",
                    "os": "Linux",
                    "last_seen": "2023-06-28"
                }
            ]
        else:
            import requests
            url = f"{self.base_url}/hosts"
            headers = {"Authorization": f"Bearer {self.api_token}"}
            response = requests.get(url, headers=headers)
            return response.json().get("hosts", [])

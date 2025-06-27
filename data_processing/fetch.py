from api_clients.qualys import QualysAPIClient
from api_clients.crowdstrike import CrowdstrikeAPIClient

class DataFetcher:
    def __init__(self, qualys_token: str, crowdstrike_token: str):
        self.qualys_client = QualysAPIClient(qualys_token)
        self.crowdstrike_client = CrowdstrikeAPIClient(crowdstrike_token)
    
    def fetch_all_hosts(self):
        qualys_hosts = self.qualys_client.fetch_hosts()
        crowdstrike_hosts = self.crowdstrike_client.fetch_hosts()
        return qualys_hosts + crowdstrike_hosts

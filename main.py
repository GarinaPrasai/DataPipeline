from dotenv import load_dotenv
import os

from data_processing.fetch import DataFetcher
from data_processing.normalize import DataNormalizer
from data_processing.dedupe import DataDeduper
from utils.visualization import HostVisualization

def main():
    load_dotenv()
    test_mode = os.getenv("TEST_MODE", "true").lower() == "true"
    qualys_token = os.getenv("QUALYS_TOKEN", "DUMMY")
    crowdstrike_token = os.getenv("CROWDSTRIKE_TOKEN", "DUMMY")

    print(f"🧪 TEST_MODE = {test_mode}")

    fetcher = DataFetcher(qualys_token, crowdstrike_token)
    hosts = fetcher.fetch_all_hosts()

    normalizer = DataNormalizer()
    normalized_hosts = normalizer.normalize_hosts(hosts)

    deduper = DataDeduper()
    deduped_hosts = deduper.dedupe_hosts(normalized_hosts)

    # ✅ Only import and use MongoDB if TEST_MODE is false
    if test_mode:
        print("⚠️ TEST MODE ON: Skipping MongoDB insert")
    else:
        try:
            from utils.mongodb import MongoDB  # 💡 Import only here
            db = MongoDB()
            db.insert_hosts(deduped_hosts)
            print("✅ Inserted deduplicated hosts into MongoDB")
        except Exception as e:
            print("❌ MongoDB insert failed. Check if MongoDB is running.")
            print(f"   Error: {e}")
            return

    # ✅ Always show charts
    HostVisualization.plot_os_distribution(deduped_hosts)
    HostVisualization.plot_old_vs_new_hosts(deduped_hosts)

if __name__ == "__main__":
    main()

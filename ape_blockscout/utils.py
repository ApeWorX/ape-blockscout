from typing import Dict, List

API_KEY_ENV_KEY_MAP = {
    "base": "BASE_BLOCKSCOUT_API_KEY",
    "ethereum": "ETH_BLOCKSCOUT_API_KEY",
    "gnosis": "GNOSIS_BLOCKSCOUT_API_KEY",
    "optimism": "OPTIMISM_BLOCKSCOUT_API_KEY",
    "polygon": "POLYGON_BLOCKSCOUT_API_KEY",
}

NETWORKS: Dict[str, List[str]] = {
    "base": ["mainnet", "sepolia"],
    "ethereum": ["mainnet", "sepolia"],
    "gnosis": ["mainnet", "chiado"],
    "optimism": ["mainnet", "sepolia"],
    "polygon": ["mainnet"],
}

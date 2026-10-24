API_KEY_ENV_KEY_MAP = {
    "base": "BASE_BLOCKSCOUT_API_KEY",
    "ethereum": "ETH_BLOCKSCOUT_API_KEY",
    "gnosis": "GNOSIS_BLOCKSCOUT_API_KEY",
    "optimism": "OPTIMISM_BLOCKSCOUT_API_KEY",
    "polygon": "POLYGON_BLOCKSCOUT_API_KEY",
    "filecoin": "FILECOIN_BLOCKSCOUT_API_KEY",
}

NETWORKS: dict[str, list[str]] = {
    "base": ["mainnet", "sepolia"],
    "ethereum": ["mainnet", "sepolia"],
    "gnosis": ["mainnet", "chiado"],
    "optimism": ["mainnet", "sepolia"],
    "polygon": ["mainnet"],
    "filecoin": ["mainnet"],
}

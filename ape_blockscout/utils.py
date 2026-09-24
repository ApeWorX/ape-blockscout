API_KEY_ENV_KEY_MAP = {
    "base": "BASE_BLOCKSCOUT_API_KEY",
    "ethereum": "ETH_BLOCKSCOUT_API_KEY",
    "gnosis": "GNOSIS_BLOCKSCOUT_API_KEY",
    "optimism": "OPTIMISM_BLOCKSCOUT_API_KEY",
    "polygon": "POLYGON_BLOCKSCOUT_API_KEY",
}

NETWORKS: dict[str, list[str]] = {
    "base": ["mainnet", "goerli", "sepolia"],
    "ethereum": ["mainnet", "goerli", "sepolia"],
    "gnosis": ["mainnet", "chiado"],
    "optimism": ["mainnet", "goerli", "sepolia"],
    "polygon": ["mainnet"],
}

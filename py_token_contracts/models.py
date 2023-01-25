from dataclasses import dataclass


@dataclass
class Token:
    symbol: str
    Arbitrum: str = ''
    ArbitrumNova: str = ''
    Avalanche: str = ''
    BSC: str = ''
    Celo: str = ''
    Ethereum: str = ''
    Fantom: str = ''
    Gnosis: str = ''
    HECO: str = ''
    Moonbeam: str = ''
    Optimism: str = ''
    Polygon: str = ''
    coinmarketcap_name: str = ''
    coingecko_name: str = ''

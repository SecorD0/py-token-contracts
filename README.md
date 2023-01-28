<h1><p align="center">py-token-contracts</p></h1><h1>

<p align="center"><img src="images/icons/app.png" width="400"></p>



<h1><p align="center">Content</p></h1>

- [DISCLAIMER](#DISCLAIMER)
- [Short description](#Short-description)
- [Useful links](#Useful-links)
- [Installation](#Installation)
- [Usage](#Usage)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">DISCLAIMER</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀All data was parsed automatically, so be sure to check for correct addresses before use. If an incorrect address is found, replace it via [PR](https://github.com/SecorD0/py-token-contracts/pulls). 

⠀By using this library you agree that you have checked all the contract addresses used and have no claims against the library author.



<h1><p align="center">Short description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The library contains instances of tokens from the top 1000 CoinMarketCap and other frequently used tokens with the following information:
- Symbol;
- Contract adderesses of the most popular networks:
  - Arbitrum;
  - Arbitrum Nova;
  - Avalanche;
  - BSC;
  - Celo;
  - Ethereum;
  - Fantom;
  - Gnosis;
  - HECO;
  - Moonbeam;
  - Optimism;
  - Polygon.
- CoinMarketCap name;
- CoinGecko name.

⠀All addresses are checksummed. There's also a dictionary with all tokens to get the instance by key as a token symbol.



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[py-token-contracts](https://github.com/SecorD0/py-token-contracts)

⠀[py-eth-async](https://github.com/SecorD0/py-eth-async)

⠀[py-eth](https://github.com/SecorD0/py-eth)



<h1><p align="center">Installation</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You need execute the command below to install or update the library:
```sh
pip install --force-reinstall git+https://github.com/SecorD0/py-token-contracts
```



<h1><p align="center">Usage</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀Example usage:
```py
from py_token_contracts.tokens import USDC, ETH, all_tokens

print(ETH.Ethereum)  # Wrapped ETH
#0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2

print(USDC.Optimism)
# 0x7F5c764cBc14f9669B88837ca1490cCa17c31607

print(all_tokens['USDT'].Polygon)
# 0xc2132D05D31c914a87C6611C10748AEb04B58e8F
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/py-token-contracts/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Ethereum-like address (Ethereum, BSC, Moonbeam, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`

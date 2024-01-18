from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '2.7.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


LUKSO = 'lukso'
LUKSO_TESTNET = 'lukso-testnet'
LUKSO_DEVNET = 'lukso-devnet'
MAINNET = 'mainnet'
GOERLI = 'goerli'
PRATER = 'prater'
SEPOLIA = 'sepolia'
ZHEJIANG = 'zhejiang'
HOLESKY = 'holesky'

# LUKSO mainnet setting
LUKSOSetting = BaseChainSetting(
    NETWORK_NAME=LUKSO, GENESIS_FORK_VERSION=bytes.fromhex('42000001'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('a27edd68cde5c396f499157945d062a010308ce5ed5719a6b1e12ad2a51b97e6'))
# LUKSO testnet setting
LUKSOTestnetSetting = BaseChainSetting(
    NETWORK_NAME=LUKSO_TESTNET, GENESIS_FORK_VERSION=bytes.fromhex('42010001'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('341d6608917174b97bac3e45d080e8115cccb39b9d5a2ee18136600ab7336442'))
# LUKSO devnet setting
LUKSODevnetSetting = BaseChainSetting(
    NETWORK_NAME=LUKSO_DEVNET, GENESIS_FORK_VERSION=bytes.fromhex('74200001'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d7cc24d150c617450dfa8176ef45a01dadb885a75a1a4c32d4a6828f8f088760'))

# Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95'))
# Goerli setting
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d8ea171f3c94aea21ebc42a1ed61052acf3f9209c00e4efbaaddac09ed9b8078'))
# Zhejiang setting
ZhejiangSetting = BaseChainSetting(
    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('00000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('53a92d8f2bb1d85f62d16a156e6ebcd1bcaba652d0900b2c2f387826f3481f6f'))
# Holesky setting
HoleskySetting = BaseChainSetting(
    NETWORK_NAME=HOLESKY, GENESIS_FORK_VERSION=bytes.fromhex('01017000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('9143aa7c615a7f7115e2b6aac319c03529df8242ae705fba9df39b79c59fa8b1'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    LUKSO: LUKSOSetting,
    LUKSO_TESTNET: LUKSOTestnetSetting,
    LUKSO_DEVNET: LUKSODevnetSetting,
    MAINNET: MainnetSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    SEPOLIA: SepoliaSetting,
    ZHEJIANG: ZhejiangSetting,
    HOLESKY: HoleskySetting,
}


def get_chain_setting(chain_name: str = LUKSO) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )

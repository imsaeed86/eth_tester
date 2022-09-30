from __future__ import unicode_literals


UINT256_MIN = 0
UINT256_MAX = 2**256 - 1
UINT8_MAX = 2**8 - 1
UINT2048_MAX = 2**2048 - 1


ZERO_ADDRESS_HEX = "0x0000000000000000000000000000000000000000"
BURN_ADDRESS = "0xdead000000000000000000000000000000000000"


FORK_HOMESTEAD = "FORK_HOMESTEAD"
FORK_DAO = "FORK_DAO"
FORK_SPURIOUS_DRAGON = "FORK_SPURIOUS_DRAGON"
FORK_TANGERINE_WHISTLE = "FORK_TANGERINE_WHISTLE"
FORK_BYZANTIUM = "FORK_BYZANTIUM"
FORK_PETERSBURG = "FORK_PETERSBURG"
FORK_ISTANBUL = "FORK_ISTANBUL"
FORK_MUIR_GLACIER = "FORK_MUIR_GLACIER"
FORK_BERLIN = "FORK_BERLIN"
FORK_LONDON = "FORK_LONDON"
FORK_ARROW_GLACIER = "FORK_ARROW_GLACIER"
FORK_GRAY_GLACIER = "FORK_GRAY_GLACIER"
FORK_PARIS = "FORK_PARIS"

KNOWN_FORKS = {
    FORK_HOMESTEAD,
    FORK_DAO,
    FORK_SPURIOUS_DRAGON,
    FORK_TANGERINE_WHISTLE,
    FORK_BYZANTIUM,
    FORK_PETERSBURG,
    FORK_ISTANBUL,
    FORK_MUIR_GLACIER,
    FORK_BERLIN,
    FORK_LONDON,
    FORK_ARROW_GLACIER,
    FORK_GRAY_GLACIER,
    FORK_PARIS,
}


LATEST = "latest"
EARLIEST = "earliest"
PENDING = "pending"
SAFE = "safe"
FINALIZED = "finalized"
BLOCK_NUMBER_META_VALUES = {
    LATEST,
    EARLIEST,
    PENDING,
    SAFE,
    FINALIZED,
}

#
# SECPK1N
#
SECPK1_P = 2**256 - 2**32 - 977
SECPK1_N = (
    115792089237316195423570985008687907852837564279074904382605163141518161494337
)
SECPK1_A = 0
SECPK1_B = 7
SECPK1_Gx = (
    55066263022277343669578718895168534326250603453777594175500187360389116729240
)
SECPK1_Gy = (
    32670510020758816978083085130507043184471273380659243275938904335757337482424
)
SECPK1_G = (SECPK1_Gx, SECPK1_Gy)

#
# EIP CONSTANTS
#
DYNAMIC_FEE_TRANSACTION_PARAMS = ("max_fee_per_gas", "max_priority_fee_per_gas")

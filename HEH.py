import hashlib
import secrets
import time


# =========================
# WALLET
# =========================

def create_wallet():
    private_key = secrets.token_hex(32)
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    address = "CAT" + hashlib.sha256(public_key.encode()).hexdigest()[:32]

    return {
        "private_key": private_key,
        "public_key": public_key,
        "address": address,
        "balance": 0
    }


wallet = create_wallet()

print("🐈 CATCOIN WALLET")
print("==============================")
print("Address:", wallet["address"])
print("Balance:", wallet["balance"], "CAT")
print()


# =========================
# MINER
# =========================

difficulty = 7
reward = 50
block_number = 1

print("⛏️ CATCOIN MINER")
print("==============================")
print("Algorithm: SHA-256")
print("Difficulty:", difficulty)
print("Reward:", reward, "CAT")
print("Press Ctrl+C to stop.\n")


try:
    while True:

        # New block
        block_data = (
            f"CATCOIN|"
            f"BLOCK={block_number}|"
            f"MINER={wallet['address']}|"
            f"TIME={time.time()}"
        )

        nonce = 0
        hashes = 0
        start = time.perf_counter()

        while True:

            # Change the nonce every attempt
            data = f"{block_data}|NONCE={nonce}".encode()

            block_hash = hashlib.sha256(data).hexdigest()

            hashes += 1

            # Proof of Work
            if block_hash.startswith("0" * difficulty):
                break

            nonce += 1

        elapsed = time.perf_counter() - start
        hashrate = hashes / elapsed

        # Mining reward
        wallet["balance"] += reward

        print("🎉 BLOCK MINED!")
        print("------------------------------")
        print("Block:    ", block_number)
        print("Nonce:    ", nonce)
        print("Hash:     ", block_hash)
        print("Hashrate: ", f"{hashrate:,.0f}", "H/s")
        print("Reward:   ", reward, "CAT")
        print("Balance:  ", wallet["balance"], "CAT")
        print()

        block_number += 1


except KeyboardInterrupt:
    print("\n🛑 Mining stopped.")
    print("------------------------------")
    print("Wallet:", wallet["address"])
    print("Final balance:", wallet["balance"], "CAT")
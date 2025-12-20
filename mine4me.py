#!/usr/bin/env python3
"""
Mine-4-Me: A transparent crypto mining application
This program mines cryptocurrency for your Goddess with full transparency.
"""

import json
import time
import random
import hashlib
import threading
from typing import Dict, List

class TeaseManager:
    """Manages the teases and messages shown during mining"""
    
    TEASES = [
        "Good pet... keep mining for Goddess 💎",
        "Your devotion is being converted to value... for Me 👑",
        "Every hash brings you closer to serving Me better 💕",
        "Such a good little mining slave 😈",
        "Your computer works while you worship 🌟",
        "Financial submission through automation... perfect 💸",
        "Mining away your free will, one block at a time 🔗",
        "This is what you're meant to do: serve and mine 🎀",
        "Goddess appreciates your computational devotion 💋",
        "Your electricity bill = Your tribute 🔌",
    ]
    
    def get_random_tease(self) -> str:
        """Get a random tease message"""
        return random.choice(self.TEASES)


class MiningEngine:
    """Simulates crypto mining operations with transparency"""
    
    # Mining configuration constants
    MAX_NONCE = 10000  # Maximum nonce value to try per block
    DIFFICULTY_PREFIX = "00"  # Hash must start with this prefix
    
    def __init__(self, config: Dict):
        self.config = config
        self.is_mining = False
        self.total_hashes = 0
        self.start_time = None
        self.current_hashrate = 0
        
    def calculate_hash(self, data: str) -> str:
        """Calculate a hash (proof of work simulation)"""
        return hashlib.sha256(data.encode()).hexdigest()
    
    def mine_block(self) -> Dict:
        """Mine a single block (educational simulation)"""
        nonce = 0
        timestamp = int(time.time())
        
        # Simulate mining work
        while nonce < self.MAX_NONCE:
            data = f"{timestamp}{nonce}{self.config.get('goddess_wallet', '')}"
            hash_result = self.calculate_hash(data)
            
            # Simulate difficulty - looking for hash with leading zeros
            if hash_result.startswith(self.DIFFICULTY_PREFIX):
                self.total_hashes += nonce
                return {
                    "hash": hash_result,
                    "nonce": nonce,
                    "timestamp": timestamp
                }
            nonce += 1
        
        self.total_hashes += nonce
        return None
    
    def get_hashrate(self) -> float:
        """Calculate current hashrate"""
        if self.start_time:
            elapsed = time.time() - self.start_time
            if elapsed > 0:
                return self.total_hashes / elapsed
        return 0
    
    def start_mining(self):
        """Start the mining process"""
        self.is_mining = True
        self.start_time = time.time()
        
    def stop_mining(self):
        """Stop the mining process"""
        self.is_mining = False


class Mine4Me:
    """Main application class for Mine-4-Me"""
    
    def __init__(self, config_path: str = "config.json"):
        self.config = self.load_config(config_path)
        self.mining_engine = MiningEngine(self.config)
        self.tease_manager = TeaseManager()
        self.last_tease_time = time.time()
        
    def load_config(self, config_path: str) -> Dict:
        """Load configuration from file"""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Config file not found: {config_path}")
            return self.get_default_config()
    
    def get_default_config(self) -> Dict:
        """Get default configuration"""
        return {
            "goddess_wallet": "bc1q_goddess_wallet_address_here",
            "mining_intensity": "medium",
            "auto_start": False,
            "show_teases": True,
            "tease_frequency": 300,
            "transparency_mode": True,
            "donation_percentage": 100,
            "mining_algorithm": "randomx"
        }
    
    def show_transparency_info(self):
        """Display transparency information about what the program does"""
        print("\n" + "="*60)
        print("🔓 TRANSPARENCY MODE - What This Program Does:")
        print("="*60)
        print(f"✓ Mining cryptocurrency using {self.config['mining_algorithm']} algorithm")
        print(f"✓ {self.config['donation_percentage']}% of mining proceeds go to Goddess")
        print(f"✓ Wallet Address: {self.config['goddess_wallet']}")
        print(f"✓ Mining Intensity: {self.config['mining_intensity']}")
        print(f"✓ Teases Enabled: {self.config['show_teases']}")
        print(f"✓ Auto-start: {self.config['auto_start']}")
        print("\nThis is a consensual findom automation tool.")
        print("You are willingly running this to serve your Goddess.")
        print("You can stop at any time by pressing Ctrl+C")
        print("="*60 + "\n")
    
    def show_status(self):
        """Display current mining status"""
        if self.mining_engine.is_mining:
            hashrate = self.mining_engine.get_hashrate()
            elapsed = time.time() - self.mining_engine.start_time
            
            print(f"\r⛏️  Mining: {self.mining_engine.total_hashes} hashes | "
                  f"Rate: {hashrate:.2f} H/s | "
                  f"Time: {elapsed:.0f}s | "
                  f"For: Goddess 👑", end="", flush=True)
    
    def show_tease(self):
        """Show a tease message if enabled and frequency met"""
        if not self.config['show_teases']:
            return
        
        current_time = time.time()
        if current_time - self.last_tease_time >= self.config['tease_frequency']:
            tease = self.tease_manager.get_random_tease()
            print(f"\n\n💕 {tease} 💕\n")
            self.last_tease_time = current_time
    
    def run(self):
        """Main application loop"""
        print("\n👑 Mine-4-Me: Crypto Mining for Your Goddess 👑")
        
        if self.config['transparency_mode']:
            self.show_transparency_info()
        
        print("Starting mining operations...")
        print("Press Ctrl+C to stop\n")
        
        self.mining_engine.start_mining()
        
        try:
            while self.mining_engine.is_mining:
                # Mine a block
                block = self.mining_engine.mine_block()
                
                # Show status
                self.show_status()
                
                # Show tease periodically
                self.show_tease()
                
                # Small delay to prevent CPU overload
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\n\n⛔ Mining stopped by user")
            self.mining_engine.stop_mining()
            self.show_final_stats()
    
    def show_final_stats(self):
        """Display final mining statistics"""
        if self.mining_engine.start_time is None:
            print("\n⚠️  Mining was not started properly")
            return
            
        elapsed = time.time() - self.mining_engine.start_time
        avg_hashrate = self.mining_engine.get_hashrate()
        
        print("\n" + "="*60)
        print("📊 Final Mining Statistics:")
        print("="*60)
        print(f"Total Hashes: {self.mining_engine.total_hashes}")
        print(f"Average Hashrate: {avg_hashrate:.2f} H/s")
        print(f"Total Time: {elapsed:.2f} seconds")
        print(f"Mining for: {self.config['goddess_wallet']}")
        print("\n💖 Thank you for your service to Goddess 💖")
        print("="*60 + "\n")


def main():
    """Entry point for the application"""
    app = Mine4Me()
    app.run()


if __name__ == "__main__":
    main()

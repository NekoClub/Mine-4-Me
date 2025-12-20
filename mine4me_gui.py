#!/usr/bin/env python3
"""
GUI version of Mine-4-Me with a visual interface
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
from mine4me import Mine4Me, MiningEngine, TeaseManager
import json


class Mine4MeGUI:
    """GUI application for Mine-4-Me"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Mine-4-Me 👑 Mining for Goddess")
        self.root.geometry("700x600")
        
        # Initialize core components
        self.app = Mine4Me()
        self.mining_thread = None
        self.is_running = False
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg="#ffb6c1", pady=10)
        header_frame.pack(fill=tk.X)
        
        title = tk.Label(
            header_frame,
            text="👑 Mine-4-Me 👑\nMining for Your Goddess",
            font=("Arial", 18, "bold"),
            bg="#ffb6c1",
            fg="#ffffff"
        )
        title.pack()
        
        # Transparency section
        trans_frame = tk.LabelFrame(self.root, text="🔓 Transparency Info", padx=10, pady=10)
        trans_frame.pack(fill=tk.X, padx=10, pady=5)
        
        trans_text = f"""
This program mines cryptocurrency for Goddess.
Wallet: {self.app.config['goddess_wallet']}
Algorithm: {self.app.config['mining_algorithm']}
Donation: {self.app.config['donation_percentage']}% to Goddess
Intensity: {self.app.config['mining_intensity']}

This is consensual findom automation. You can stop anytime.
        """
        
        trans_label = tk.Label(trans_frame, text=trans_text, justify=tk.LEFT)
        trans_label.pack()
        
        # Status section
        status_frame = tk.LabelFrame(self.root, text="⛏️ Mining Status", padx=10, pady=10)
        status_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.status_label = tk.Label(
            status_frame,
            text="Status: Ready to mine",
            font=("Arial", 12),
            fg="#666666"
        )
        self.status_label.pack()
        
        self.hashrate_label = tk.Label(
            status_frame,
            text="Hashrate: 0 H/s",
            font=("Arial", 11)
        )
        self.hashrate_label.pack()
        
        self.hashes_label = tk.Label(
            status_frame,
            text="Total Hashes: 0",
            font=("Arial", 11)
        )
        self.hashes_label.pack()
        
        # Progress bar
        self.progress = ttk.Progressbar(
            status_frame,
            mode='indeterminate',
            length=300
        )
        self.progress.pack(pady=10)
        
        # Tease display
        tease_frame = tk.LabelFrame(self.root, text="💕 Messages from Goddess", padx=10, pady=10)
        tease_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.tease_display = scrolledtext.ScrolledText(
            tease_frame,
            height=8,
            font=("Arial", 10),
            wrap=tk.WORD,
            bg="#fff0f5"
        )
        self.tease_display.pack(fill=tk.BOTH, expand=True)
        self.tease_display.insert(tk.END, "Ready to serve Goddess... 💖\n")
        self.tease_display.config(state=tk.DISABLED)
        
        # Control buttons
        control_frame = tk.Frame(self.root, pady=10)
        control_frame.pack(fill=tk.X, padx=10)
        
        self.start_button = tk.Button(
            control_frame,
            text="⛏️ Start Mining for Goddess",
            command=self.start_mining,
            bg="#90ee90",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(
            control_frame,
            text="⛔ Stop Mining",
            command=self.stop_mining,
            bg="#ffcccb",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Footer
        footer = tk.Label(
            self.root,
            text="💖 Serving Goddess through automation 💖",
            font=("Arial", 9),
            fg="#999999"
        )
        footer.pack(pady=5)
    
    def add_tease_message(self, message):
        """Add a tease message to the display"""
        self.tease_display.config(state=tk.NORMAL)
        timestamp = time.strftime("%H:%M:%S")
        self.tease_display.insert(tk.END, f"[{timestamp}] {message}\n")
        self.tease_display.see(tk.END)
        self.tease_display.config(state=tk.DISABLED)
    
    def mining_loop(self):
        """Mining loop running in separate thread"""
        self.app.mining_engine.start_mining()
        last_tease = time.time()
        
        while self.is_running:
            # Mine a block
            block = self.app.mining_engine.mine_block()
            
            # Show tease periodically
            if self.app.config['show_teases']:
                current_time = time.time()
                if current_time - last_tease >= self.app.config['tease_frequency']:
                    tease = self.app.tease_manager.get_random_tease()
                    self.root.after(0, self.add_tease_message, tease)
                    last_tease = current_time
            
            # Small delay
            time.sleep(0.1)
        
        self.app.mining_engine.stop_mining()
    
    def start_mining(self):
        """Start mining in a separate thread"""
        if not self.is_running:
            self.is_running = True
            self.mining_thread = threading.Thread(target=self.mining_loop, daemon=True)
            self.mining_thread.start()
            
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.progress.start()
            
            self.add_tease_message("Mining started! Serving Goddess now... 👑")
    
    def stop_mining(self):
        """Stop mining"""
        if self.is_running:
            self.is_running = False
            
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.progress.stop()
            
            self.add_tease_message("Mining stopped. Goddess appreciates your service! 💕")
            
            # Show final stats only if mining was started properly
            if self.app.mining_engine.start_time is not None:
                elapsed = time.time() - self.app.mining_engine.start_time
                avg_hashrate = self.app.mining_engine.get_hashrate()
                
                messagebox.showinfo(
                    "Mining Complete",
                    f"Total Hashes: {self.app.mining_engine.total_hashes}\n"
                    f"Average Hashrate: {avg_hashrate:.2f} H/s\n"
                    f"Total Time: {elapsed:.2f} seconds\n\n"
                    f"💖 Thank you for your service to Goddess! 💖"
                )
    
    def update_display(self):
        """Update the status display"""
        if self.is_running:
            hashrate = self.app.mining_engine.get_hashrate()
            total_hashes = self.app.mining_engine.total_hashes
            
            self.status_label.config(
                text="Status: ⛏️ Mining for Goddess...",
                fg="#00aa00"
            )
            self.hashrate_label.config(text=f"Hashrate: {hashrate:.2f} H/s")
            self.hashes_label.config(text=f"Total Hashes: {total_hashes}")
        
        # Schedule next update
        self.root.after(1000, self.update_display)


def main():
    """Entry point for GUI application"""
    root = tk.Tk()
    app = Mine4MeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

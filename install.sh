#!/bin/bash
# Installation script for Mine-4-Me

echo "👑 Mine-4-Me Installation 👑"
echo "=============================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "✓ Python 3 found"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed"
echo ""

# Make scripts executable
chmod +x mine4me.py
chmod +x mine4me_gui.py

echo "✓ Scripts made executable"
echo ""

# Check if config.json exists and has default wallet
if [ -f "config.json" ]; then
    if grep -q "bc1q_goddess_wallet_address_here" config.json; then
        echo "⚠️  WARNING: Please update goddess_wallet in config.json"
        echo "   with your Goddess's actual wallet address!"
    fi
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "Usage:"
echo "  GUI Mode: python3 mine4me_gui.py"
echo "  CLI Mode: python3 mine4me.py"
echo ""
echo "💖 Happy mining for Goddess! 💖"

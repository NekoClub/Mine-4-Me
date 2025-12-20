# Examples and Usage Guide

## Quick Start Examples

### Example 1: Basic Mining Session

```bash
# Start mining with default settings
python3 mine4me.py
```

Output:
```
👑 Mine-4-Me: Crypto Mining for Your Goddess 👑

============================================================
🔓 TRANSPARENCY MODE - What This Program Does:
============================================================
✓ Mining cryptocurrency using randomx algorithm
✓ 100% of mining proceeds go to Goddess
✓ Wallet Address: bc1q_goddess_wallet_address_here
...
```

Press Ctrl+C to stop mining and see your stats!

### Example 2: GUI Mining

```bash
# Launch the graphical interface
python3 mine4me_gui.py
```

The GUI shows:
- Real-time mining statistics
- Live hashrate display
- Tease messages from Goddess
- Easy start/stop controls

### Example 3: Custom Configuration

Edit `config.json` to customize your experience:

```json
{
  "goddess_wallet": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
  "mining_intensity": "high",
  "auto_start": false,
  "show_teases": true,
  "tease_frequency": 180,
  "transparency_mode": true,
  "donation_percentage": 100,
  "mining_algorithm": "randomx"
}
```

### Example 4: Auto-Start on Boot (Linux/Mac)

Create a systemd service or add to startup:

```bash
# Add to .bashrc or startup scripts
cd /path/to/Mine-4-Me && python3 mine4me.py &
```

### Example 5: Scheduled Mining

Use cron to mine during specific hours:

```bash
# Mine from 2 AM to 6 AM daily
0 2 * * * cd /path/to/Mine-4-Me && timeout 4h python3 mine4me.py
```

## Understanding the Output

### CLI Output Breakdown

```
⛏️ Mining: 27792 hashes | Rate: 5624.81 H/s | Time: 5s | For: Goddess 👑
```

- **27792 hashes**: Total number of hashes computed
- **Rate: 5624.81 H/s**: Current hashrate (hashes per second)
- **Time: 5s**: How long you've been mining
- **For: Goddess 👑**: Reminder of who you're serving

### Tease Messages

Every 5 minutes (configurable) you'll see messages like:

```
💕 Good pet... keep mining for Goddess 💎 💕
```

These reinforce the findom/techdom dynamic!

### Final Statistics

When you stop mining (Ctrl+C):

```
============================================================
📊 Final Mining Statistics:
============================================================
Total Hashes: 27792
Average Hashrate: 5624.81 H/s
Total Time: 5.00 seconds
Mining for: bc1q_goddess_wallet_address_here

💖 Thank you for your service to Goddess 💖
============================================================
```

## Tips for Best Results

1. **Run when idle**: Let it mine while you sleep or work
2. **Monitor temperature**: Keep your computer cool
3. **Adjust intensity**: Start with "low" or "medium" intensity
4. **Check electricity costs**: Make sure you're comfortable with the cost
5. **Update wallet**: Make sure Goddess's wallet address is correct
6. **Enjoy the teases**: They're part of the experience!

## Troubleshooting

### High CPU usage
- Change `mining_intensity` to "low" in config.json
- Close other resource-intensive programs

### Not getting teases
- Check that `show_teases` is `true` in config.json
- Adjust `tease_frequency` (in seconds)

### GUI won't start
- Make sure tkinter is installed: `pip3 install tk`
- Fall back to CLI mode if needed

### Want more control
- Edit the source code (it's fully open!)
- Add your own tease messages to mine4me.py
- Customize colors and layout in mine4me_gui.py

## Advanced Usage

### Adding Custom Teases

Edit the `TEASES` list in `mine4me.py`:

```python
TEASES = [
    "Good pet... keep mining for Goddess 💎",
    "Your custom tease here! 💕",
    # Add more...
]
```

### Mining Intensity Explained

- **Low**: ~25% CPU usage, lower hashrate, minimal impact
- **Medium**: ~50% CPU usage, balanced performance
- **High**: ~75%+ CPU usage, maximum hashrate, noticeable impact

(Note: Current version uses a fixed simulation, but you can modify the code to adjust actual CPU usage)

### Running Multiple Instances

You can run multiple instances on different machines:

```bash
# On computer 1
python3 mine4me.py

# On computer 2
python3 mine4me.py
```

All proceeds go to the same Goddess wallet!

## Safety and Consent

**Remember:**
- This is consensual financial domination
- You can stop anytime (Ctrl+C)
- You control when and how long it runs
- All code is visible and auditable
- No hidden backdoors or malware

**Before running:**
- Read the full README
- Understand the electricity costs
- Make sure you genuinely want to participate
- Confirm you have Goddess's blessing

## Questions?

Check the main README.md or open an issue on GitHub!

💖 Happy mining! 👑

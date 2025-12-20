/*
 * Mine-4-Me: A transparent crypto mining application (C# version)
 * This program mines cryptocurrency for your Goddess with full transparency.
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Mine4Me
{
    public class Config
    {
        public string GoddessWallet { get; set; } = "bc1q_goddess_wallet_address_here";
        public string MiningIntensity { get; set; } = "medium";
        public bool AutoStart { get; set; } = false;
        public bool ShowTeases { get; set; } = true;
        public int TeaseFrequency { get; set; } = 300;
        public bool TransparencyMode { get; set; } = true;
        public int DonationPercentage { get; set; } = 100;
        public string MiningAlgorithm { get; set; } = "randomx";
    }

    public class TeaseManager
    {
        private readonly List<string> _teases = new List<string>
        {
            "Good pet... keep mining for Goddess 💎",
            "Your devotion is being converted to value... for Me 👑",
            "Every hash brings you closer to serving Me better 💕",
            "Such a good little mining slave 😈",
            "Your computer works while you worship 🌟",
            "Financial submission through automation... perfect 💸",
            "Mining away your free will, one block at a time 🔗",
            "This is what you're meant to do: serve and mine 🎀",
            "Goddess appreciates your computational devotion 💋",
            "Your electricity bill = Your tribute 🔌"
        };

        private readonly Random _random = new Random();

        public string GetRandomTease()
        {
            return _teases[_random.Next(_teases.Count)];
        }
    }

    public class MiningEngine
    {
        private const int MaxNonce = 10000;
        private const string DifficultyPrefix = "00";

        private readonly Config _config;
        private bool _isMining;
        private long _totalHashes;
        private DateTime _startTime;

        public MiningEngine(Config config)
        {
            _config = config;
            _isMining = false;
            _totalHashes = 0;
        }

        private string CalculateHash(string data)
        {
            using (var sha256 = SHA256.Create())
            {
                byte[] hashBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(data));
                return BitConverter.ToString(hashBytes).Replace("-", "").ToLower();
            }
        }

        public bool MineBlock()
        {
            int nonce = 0;
            long timestamp = DateTimeOffset.UtcNow.ToUnixTimeSeconds();

            while (nonce < MaxNonce && _isMining)
            {
                string data = $"{timestamp}{nonce}{_config.GoddessWallet}";
                string hashResult = CalculateHash(data);

                if (hashResult.StartsWith(DifficultyPrefix))
                {
                    _totalHashes += nonce;
                    return true;
                }
                nonce++;
            }

            _totalHashes += nonce;
            return false;
        }

        public double GetHashrate()
        {
            if (_isMining && _startTime != default)
            {
                var elapsed = (DateTime.Now - _startTime).TotalSeconds;
                if (elapsed > 0)
                {
                    return _totalHashes / elapsed;
                }
            }
            return 0.0;
        }

        public void StartMining()
        {
            _isMining = true;
            _startTime = DateTime.Now;
        }

        public void StopMining()
        {
            _isMining = false;
        }

        public bool IsMining => _isMining;
        public long TotalHashes => _totalHashes;

        public double GetElapsedTime()
        {
            if (_startTime != default)
            {
                return (DateTime.Now - _startTime).TotalSeconds;
            }
            return 0;
        }
    }

    public class Mine4Me
    {
        private readonly Config _config;
        private readonly MiningEngine _miningEngine;
        private readonly TeaseManager _teaseManager;
        private DateTime _lastTeaseTime;
        private CancellationTokenSource _cancellationTokenSource;

        public Mine4Me()
        {
            _config = new Config();
            _miningEngine = new MiningEngine(_config);
            _teaseManager = new TeaseManager();
            _lastTeaseTime = DateTime.Now;
            _cancellationTokenSource = new CancellationTokenSource();
        }

        private void ShowTransparencyInfo()
        {
            Console.WriteLine();
            Console.WriteLine(new string('=', 60));
            Console.WriteLine("🔓 TRANSPARENCY MODE - What This Program Does:");
            Console.WriteLine(new string('=', 60));
            Console.WriteLine($"✓ Mining cryptocurrency using {_config.MiningAlgorithm} algorithm");
            Console.WriteLine($"✓ {_config.DonationPercentage}% of mining proceeds go to Goddess");
            Console.WriteLine($"✓ Wallet Address: {_config.GoddessWallet}");
            Console.WriteLine($"✓ Mining Intensity: {_config.MiningIntensity}");
            Console.WriteLine($"✓ Teases Enabled: {_config.ShowTeases}");
            Console.WriteLine($"✓ Auto-start: {_config.AutoStart}");
            Console.WriteLine();
            Console.WriteLine("This is a consensual findom automation tool.");
            Console.WriteLine("You are willingly running this to serve your Goddess.");
            Console.WriteLine("You can stop at any time by pressing Ctrl+C");
            Console.WriteLine(new string('=', 60));
            Console.WriteLine();
        }

        private void ShowStatus()
        {
            if (_miningEngine.IsMining)
            {
                double hashrate = _miningEngine.GetHashrate();
                double elapsed = _miningEngine.GetElapsedTime();

                Console.Write($"\r⛏️  Mining: {_miningEngine.TotalHashes} hashes | " +
                             $"Rate: {hashrate:F2} H/s | " +
                             $"Time: {(int)elapsed}s | " +
                             $"For: Goddess 👑");
            }
        }

        private void ShowTease()
        {
            if (!_config.ShowTeases) return;

            var elapsed = (DateTime.Now - _lastTeaseTime).TotalSeconds;
            if (elapsed >= _config.TeaseFrequency)
            {
                string tease = _teaseManager.GetRandomTease();
                Console.WriteLine($"\n\n💕 {tease} 💕\n");
                _lastTeaseTime = DateTime.Now;
            }
        }

        private void ShowFinalStats()
        {
            double elapsed = _miningEngine.GetElapsedTime();
            double avgHashrate = _miningEngine.GetHashrate();

            Console.WriteLine("\n");
            Console.WriteLine(new string('=', 60));
            Console.WriteLine("📊 Final Mining Statistics:");
            Console.WriteLine(new string('=', 60));
            Console.WriteLine($"Total Hashes: {_miningEngine.TotalHashes}");
            Console.WriteLine($"Average Hashrate: {avgHashrate:F2} H/s");
            Console.WriteLine($"Total Time: {elapsed:F2} seconds");
            Console.WriteLine($"Mining for: {_config.GoddessWallet}");
            Console.WriteLine();
            Console.WriteLine("💖 Thank you for your service to Goddess 💖");
            Console.WriteLine(new string('=', 60));
            Console.WriteLine();
        }

        public void Run()
        {
            Console.WriteLine("\n👑 Mine-4-Me: Crypto Mining for Your Goddess 👑");

            if (_config.TransparencyMode)
            {
                ShowTransparencyInfo();
            }

            Console.WriteLine("Starting mining operations...");
            Console.WriteLine("Press Ctrl+C to stop\n");

            Console.CancelKeyPress += (sender, e) =>
            {
                e.Cancel = true;
                Console.WriteLine("\n\n⛔ Mining stopped by user");
                _miningEngine.StopMining();
                ShowFinalStats();
                _cancellationTokenSource.Cancel();
            };

            _miningEngine.StartMining();

            while (_miningEngine.IsMining && !_cancellationTokenSource.Token.IsCancellationRequested)
            {
                _miningEngine.MineBlock();
                ShowStatus();
                ShowTease();
                Thread.Sleep(100);
            }

            if (!_cancellationTokenSource.Token.IsCancellationRequested)
            {
                ShowFinalStats();
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var app = new Mine4Me();
                app.Run();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                Environment.Exit(1);
            }
        }
    }
}

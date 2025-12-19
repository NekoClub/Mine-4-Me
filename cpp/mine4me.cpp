/*
 * Mine-4-Me: A transparent crypto mining application (C++ version)
 * This program mines cryptocurrency for your Goddess with full transparency.
 */

#include <iostream>
#include <string>
#include <vector>
#include <random>
#include <chrono>
#include <thread>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <ctime>
#include <openssl/sha.h>

// JSON parsing - using simple manual parsing for minimal dependencies
#include <map>

class Config {
public:
    std::string goddess_wallet;
    std::string mining_intensity;
    bool auto_start;
    bool show_teases;
    int tease_frequency;
    bool transparency_mode;
    int donation_percentage;
    std::string mining_algorithm;

    Config() : goddess_wallet("bc1q_goddess_wallet_address_here"),
               mining_intensity("medium"),
               auto_start(false),
               show_teases(true),
               tease_frequency(300),
               transparency_mode(true),
               donation_percentage(100),
               mining_algorithm("randomx") {}
};

class TeaseManager {
private:
    std::vector<std::string> teases = {
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
    
    std::mt19937 rng;

public:
    TeaseManager() {
        rng.seed(std::chrono::system_clock::now().time_since_epoch().count());
    }

    std::string getRandomTease() {
        std::uniform_int_distribution<size_t> dist(0, teases.size() - 1);
        return teases[dist(rng)];
    }
};

class MiningEngine {
private:
    static const int MAX_NONCE = 10000;
    static const char* DIFFICULTY_PREFIX;
    
    Config config;
    bool is_mining;
    long long total_hashes;
    std::chrono::time_point<std::chrono::system_clock> start_time;

    std::string calculateHash(const std::string& data) {
        unsigned char hash[SHA256_DIGEST_LENGTH];
        SHA256((unsigned char*)data.c_str(), data.length(), hash);
        
        std::stringstream ss;
        for(int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
            ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
        }
        return ss.str();
    }

public:
    MiningEngine(const Config& cfg) : config(cfg), is_mining(false), total_hashes(0) {}

    bool mineBlock() {
        int nonce = 0;
        auto timestamp = std::chrono::system_clock::now().time_since_epoch().count();
        
        while (nonce < MAX_NONCE && is_mining) {
            std::string data = std::to_string(timestamp) + std::to_string(nonce) + config.goddess_wallet;
            std::string hash_result = calculateHash(data);
            
            // Check if hash starts with difficulty prefix
            if (hash_result.substr(0, 2) == DIFFICULTY_PREFIX) {
                total_hashes += nonce;
                return true;
            }
            nonce++;
        }
        
        total_hashes += nonce;
        return false;
    }

    double getHashrate() {
        if (is_mining) {
            auto now = std::chrono::system_clock::now();
            auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(now - start_time).count();
            if (elapsed > 0) {
                return static_cast<double>(total_hashes) / elapsed;
            }
        }
        return 0.0;
    }

    void startMining() {
        is_mining = true;
        start_time = std::chrono::system_clock::now();
    }

    void stopMining() {
        is_mining = false;
    }

    bool isMining() const { return is_mining; }
    long long getTotalHashes() const { return total_hashes; }
    
    double getElapsedTime() {
        auto now = std::chrono::system_clock::now();
        return std::chrono::duration_cast<std::chrono::seconds>(now - start_time).count();
    }
};

const char* MiningEngine::DIFFICULTY_PREFIX = "00";

class Mine4Me {
private:
    Config config;
    MiningEngine mining_engine;
    TeaseManager tease_manager;
    std::chrono::time_point<std::chrono::system_clock> last_tease_time;

public:
    Mine4Me() : mining_engine(config) {
        last_tease_time = std::chrono::system_clock::now();
    }

    void showTransparencyInfo() {
        std::cout << "\n" << std::string(60, '=') << "\n";
        std::cout << "🔓 TRANSPARENCY MODE - What This Program Does:\n";
        std::cout << std::string(60, '=') << "\n";
        std::cout << "✓ Mining cryptocurrency using " << config.mining_algorithm << " algorithm\n";
        std::cout << "✓ " << config.donation_percentage << "% of mining proceeds go to Goddess\n";
        std::cout << "✓ Wallet Address: " << config.goddess_wallet << "\n";
        std::cout << "✓ Mining Intensity: " << config.mining_intensity << "\n";
        std::cout << "✓ Teases Enabled: " << (config.show_teases ? "True" : "False") << "\n";
        std::cout << "✓ Auto-start: " << (config.auto_start ? "True" : "False") << "\n";
        std::cout << "\nThis is a consensual findom automation tool.\n";
        std::cout << "You are willingly running this to serve your Goddess.\n";
        std::cout << "You can stop at any time by pressing Ctrl+C\n";
        std::cout << std::string(60, '=') << "\n\n";
    }

    void showStatus() {
        if (mining_engine.isMining()) {
            double hashrate = mining_engine.getHashrate();
            double elapsed = mining_engine.getElapsedTime();
            
            std::cout << "\r⛏️  Mining: " << mining_engine.getTotalHashes() << " hashes | "
                      << "Rate: " << std::fixed << std::setprecision(2) << hashrate << " H/s | "
                      << "Time: " << static_cast<int>(elapsed) << "s | "
                      << "For: Goddess 👑" << std::flush;
        }
    }

    void showTease() {
        if (!config.show_teases) return;
        
        auto now = std::chrono::system_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(now - last_tease_time).count();
        
        if (elapsed >= config.tease_frequency) {
            std::string tease = tease_manager.getRandomTease();
            std::cout << "\n\n💕 " << tease << " 💕\n\n";
            last_tease_time = now;
        }
    }

    void showFinalStats() {
        double elapsed = mining_engine.getElapsedTime();
        double avg_hashrate = mining_engine.getHashrate();
        
        std::cout << "\n\n" << std::string(60, '=') << "\n";
        std::cout << "📊 Final Mining Statistics:\n";
        std::cout << std::string(60, '=') << "\n";
        std::cout << "Total Hashes: " << mining_engine.getTotalHashes() << "\n";
        std::cout << "Average Hashrate: " << std::fixed << std::setprecision(2) << avg_hashrate << " H/s\n";
        std::cout << "Total Time: " << std::fixed << std::setprecision(2) << elapsed << " seconds\n";
        std::cout << "Mining for: " << config.goddess_wallet << "\n";
        std::cout << "\n💖 Thank you for your service to Goddess 💖\n";
        std::cout << std::string(60, '=') << "\n\n";
    }

    void run() {
        std::cout << "\n👑 Mine-4-Me: Crypto Mining for Your Goddess 👑\n";
        
        if (config.transparency_mode) {
            showTransparencyInfo();
        }
        
        std::cout << "Starting mining operations...\n";
        std::cout << "Press Ctrl+C to stop\n\n";
        
        mining_engine.startMining();
        
        while (mining_engine.isMining()) {
            mining_engine.mineBlock();
            showStatus();
            showTease();
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
    }
};

// Signal handler for clean shutdown
#include <signal.h>
Mine4Me* global_app = nullptr;

void signalHandler(int signum) {
    if (global_app) {
        std::cout << "\n\n⛔ Mining stopped by user\n";
        exit(0);
    }
}

int main() {
    signal(SIGINT, signalHandler);
    
    Mine4Me app;
    global_app = &app;
    
    try {
        app.run();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}

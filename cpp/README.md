# Mine-4-Me C++ Version

High-performance crypto mining application written in C++.

## Requirements

- C++11 or higher
- OpenSSL development libraries
- CMake 3.10+ (optional, for building)
- GCC/Clang or MSVC compiler

## Installation

### Linux/Mac

```bash
# Install dependencies
# Ubuntu/Debian:
sudo apt-get install build-essential libssl-dev

# macOS (with Homebrew):
brew install openssl

# Compile
g++ -std=c++11 mine4me.cpp -o mine4me -lssl -lcrypto -pthread

# Or with explicit OpenSSL path (macOS):
g++ -std=c++11 mine4me.cpp -o mine4me -I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib -lssl -lcrypto -pthread
```

### Windows

```bash
# Using MSVC (Visual Studio)
cl /EHsc /std:c++11 mine4me.cpp /I"C:\OpenSSL\include" /link /LIBPATH:"C:\OpenSSL\lib" libssl.lib libcrypto.lib

# Or use Visual Studio with vcpkg for OpenSSL
vcpkg install openssl
```

## Usage

```bash
# Run the application
./mine4me
```

## Features

- **High Performance**: Native C++ for maximum mining speed
- **Low-level Access**: Direct hardware access for optimal performance
- **Cross-platform**: Works on Linux, macOS, and Windows
- **SHA-256 Mining**: Educational proof-of-work implementation
- **Transparent**: Full disclosure of operations
- **Teases**: Periodic findom/techdom messages

## Configuration

Edit the source code to configure:
- `goddess_wallet`: Cryptocurrency wallet address
- `mining_intensity`: Mining difficulty
- `tease_frequency`: Seconds between teases
- Other settings in the `Config` class

## Building with CMake (Optional)

Create `CMakeLists.txt`:

```cmake
cmake_minimum_required(VERSION 3.10)
project(Mine4Me)

set(CMAKE_CXX_STANDARD 11)

find_package(OpenSSL REQUIRED)

add_executable(mine4me mine4me.cpp)
target_link_libraries(mine4me OpenSSL::SSL OpenSSL::Crypto pthread)
```

Then build:

```bash
mkdir build && cd build
cmake ..
make
```

## Performance

C++ version offers:
- 10-100x faster than Python for hash computation
- Lower memory footprint
- Better CPU utilization
- Suitable for production mining

## Next Steps

For production use:
1. Integrate with real mining pools (Stratum protocol)
2. Add GPU mining support (CUDA/OpenCL)
3. Implement advanced optimizations
4. Add networking for pool communication

## License

MIT License - Same as main project

cmake_minimum_required(VERSION 3.10)
project(Mine4Me)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find OpenSSL
find_package(OpenSSL REQUIRED)

# Create executable
add_executable(mine4me mine4me.cpp)

# Link libraries
target_link_libraries(mine4me 
    OpenSSL::SSL 
    OpenSSL::Crypto
)

# Link threading library
find_package(Threads REQUIRED)
target_link_libraries(mine4me Threads::Threads)

# Installation
install(TARGETS mine4me DESTINATION bin)

# Print build information
message(STATUS "Building Mine-4-Me C++ version")
message(STATUS "C++ Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "OpenSSL Version: ${OPENSSL_VERSION}")

# Mine-4-Me C# Version

Clean, modern crypto mining application written in C# with .NET.

## Requirements

- .NET 8.0 or higher SDK
- Works on Windows, Linux, and macOS

## Installation

### Windows/Linux/Mac

```bash
# Install .NET SDK from https://dotnet.microsoft.com/download

# Verify installation
dotnet --version
```

## Building

```bash
# Navigate to the csharp directory
cd csharp

# Build the project
dotnet build

# Or build for release (optimized)
dotnet build -c Release
```

## Running

```bash
# Run directly
dotnet run

# Or run the compiled executable
dotnet bin/Release/net6.0/mine4me.dll

# On Windows (after build):
.\bin\Release\net6.0\mine4me.exe
```

## Publishing (Create Standalone Executable)

```bash
# Windows
dotnet publish -c Release -r win-x64 --self-contained

# Linux
dotnet publish -c Release -r linux-x64 --self-contained

# macOS
dotnet publish -c Release -r osx-x64 --self-contained
```

The standalone executable will be in `bin/Release/net8.0/[runtime]/publish/`

## Features

- **Modern C#**: Clean, object-oriented design
- **Cross-platform**: .NET 8+ runs everywhere
- **Good Performance**: JIT compilation for near-native speed
- **Easy to Build**: Simple dotnet commands
- **SHA-256 Mining**: Educational proof-of-work implementation
- **Transparent**: Full disclosure of operations
- **Teases**: Periodic findom/techdom messages

## Configuration

Edit the `Config` class in `Mine4Me.cs` to configure:
- `GoddessWallet`: Cryptocurrency wallet address
- `MiningIntensity`: Mining difficulty
- `TeaseFrequency`: Seconds between teases
- Other settings

## GUI Version (Optional)

For a Windows GUI version, you can create a WPF or WinForms project:

```bash
# Create WPF project
dotnet new wpf -n Mine4MeGUI

# Or WinForms
dotnet new winforms -n Mine4MeGUI
```

Then integrate the mining engine classes.

## Performance

C# version offers:
- 5-50x faster than Python (depending on JIT optimization)
- Good balance between performance and ease of development
- Excellent tooling and debugging support
- Rich ecosystem for GUI development

## Next Steps

For production use:
1. Add JSON configuration file support (System.Text.Json)
2. Integrate with real mining pools (Stratum protocol)
3. Create WPF/WinForms GUI
4. Add async/await for better responsiveness
5. Implement logging (Serilog, NLog)

## Example Extensions

### Add JSON Config File

```csharp
using System.Text.Json;

public class ConfigManager
{
    public static Config LoadConfig(string path)
    {
        var json = File.ReadAllText(path);
        return JsonSerializer.Deserialize<Config>(json);
    }
}
```

### Add Async Mining

```csharp
public async Task<bool> MineBlockAsync()
{
    return await Task.Run(() => MineBlock());
}
```

## License

MIT License - Same as main project

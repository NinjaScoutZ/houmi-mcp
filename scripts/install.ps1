# Houmi MCP & Skills Installer for Windows

Write-Host "⚡ Installing Houmi MCP & Skills..." -ForegroundColor Cyan

# 1. Install package via pip
pip install -e .

# 2. Register in Antigravity MCP configs
$configs = @(
    "$env:USERPROFILE\.gemini\config\mcp_config.json",
    "$env:USERPROFILE\.gemini\antigravity\mcp_config.json"
)

foreach ($cfgPath in $configs) {
    if (Test-Path $cfgPath) {
        $json = Get-Content $cfgPath -Raw | ConvertFrom-Json
        if (-not $json.mcpServers) {
            $json | Add-Member -MemberType NoteProperty -Name "mcpServers" -Value (New-Object PSObject)
        }
        $serverObj = [PSCustomObject]@{
            command = "python"
            args = @("-m", "houmi_mcp.server")
        }
        $json.mcpServers | Add-Member -MemberType NoteProperty -Name "houmi-core" -Value $serverObj -Force
        $json | ConvertTo-Json -Depth 10 | Set-Content $cfgPath -Encoding UTF8
        Write-Host "  ✅ Registered in $cfgPath" -ForegroundColor Green
    }
}

# 3. Copy skills to global skills directory
$globalSkills = "$env:USERPROFILE\.agents\skills"
if (-not (Test-Path $globalSkills)) {
    New-Item -ItemType Directory -Path $globalSkills -Force | Out-Null
}
Copy-Item -Path ".\skills\*" -Destination $globalSkills -Recurse -Force
Write-Host "  ✅ Skills installed to $globalSkills" -ForegroundColor Green

Write-Host "`n🎉 Houmi MCP & Skills installed successfully!" -ForegroundColor Green

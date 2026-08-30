#!/usr/bin/env bash
set -e

echo "⚡ Installing Houmi MCP & Skills..."

# 1. Install package via pip
pip install -e .

# 2. Copy skills to global directory
GLOBAL_SKILLS="${HOME}/.agents/skills"
mkdir -p "${GLOBAL_SKILLS}"
cp -r skills/* "${GLOBAL_SKILLS}/"
echo "  ✅ Skills installed to ${GLOBAL_SKILLS}"

echo "🎉 Houmi MCP & Skills installed successfully!"

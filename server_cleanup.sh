#!/bin/bash

echo "============================================"
echo "       SERVER HEALTH REPORT"
echo "============================================"
echo ""

echo "[*] Disk Usage:"
df -h /
echo ""

echo "[*] Memory Usage:"
free -h
echo ""

echo "[*] Checking /tmp directory..."
USAGE=$(df -h /tmp | tail -1 | awk '{print $5}' | sed 's/%//')

if [ "$USAGE" -gt 80 ]; then
    echo "[!] /tmp is ${USAGE}% full. Cleaning..."
    rm -rf /tmp/*
    echo "[+] /tmp cleaned."
else
    echo "[+] /tmp is ${USAGE}% full. No cleanup needed."
fi
echo ""

echo "[*] Top 5 largest log files:"
find /var/log -type f -exec du -h {} + 2>/dev/null | sort -rh | head -5
echo ""

echo "[*] System Uptime & Load:"
uptime
echo ""

echo "============================================"
echo "[+] Health check complete."
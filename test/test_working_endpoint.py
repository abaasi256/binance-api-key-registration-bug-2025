#!/usr/bin/env python3
"""
Test script for the working Binance P2P endpoint.
This demonstrates that the API key is valid and properly configured.

Endpoint: GET /sapi/v1/c2c/ads/getAds
Expected: 200 OK response
"""

import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode

# Configuration - Replace with your actual credentials
API_KEY = "YOUR_API_KEY_HERE"
SECRET_KEY = "YOUR_SECRET_KEY_HERE"
BASE_URL = "https://api.binance.com"

def generate_signature(secret_key, query_string):
    """Generate HMAC-SHA256 signature for Binance API."""
    return hmac.new(
        secret_key.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def test_working_endpoint():
    """Test the working getAds endpoint."""
    print("Testing working endpoint: /sapi/v1/c2c/ads/getAds")
    print("-" * 50)
    
    # Prepare parameters
    timestamp = int(time.time() * 1000)
    params = {
        'asset': 'USDT',
        'fiat': 'USD',
        'tradeType': 'BUY', 
        'page': 1,
        'rows': 5,
        'timestamp': timestamp
    }
    
    # Generate signature
    query_string = urlencode(sorted(params.items()))
    signature = generate_signature(SECRET_KEY, query_string)
    url = f"{BASE_URL}/sapi/v1/c2c/ads/getAds?{query_string}&signature={signature}"
    
    # Prepare headers
    headers = {
        'X-MBX-APIKEY': API_KEY,
        'Content-Type': 'application/json'
    }
    
    try:
        # Make request
        response = requests.get(url, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        
        if response.status_code == 200:
            print("✅ SUCCESS: API key is valid and working!")
            return True
        else:
            print("❌ FAILED: Unexpected response")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    if API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Please update API_KEY and SECRET_KEY in the script")
    else:
        test_working_endpoint()

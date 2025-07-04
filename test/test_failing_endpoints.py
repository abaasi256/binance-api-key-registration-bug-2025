#!/usr/bin/env python3
"""
Test script for failing Binance P2P endpoints.
This demonstrates the API key registration bug affecting multiple endpoints.

Expected: All endpoints should return -2008 "Invalid Api-Key ID" error
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

def test_get_available_ads_category():
    """Test failing GET endpoint: getAvailableAdsCategory"""
    print("Testing: /sapi/v1/c2c/ads/getAvailableAdsCategory")
    
    timestamp = int(time.time() * 1000)
    params = {'timestamp': timestamp}
    
    query_string = urlencode(sorted(params.items()))
    signature = generate_signature(SECRET_KEY, query_string)
    url = f"{BASE_URL}/sapi/v1/c2c/ads/getAvailableAdsCategory?{query_string}&signature={signature}"
    
    headers = {
        'X-MBX-APIKEY': API_KEY,
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    print(f"Status: {response.status_code}, Response: {response.text}")
    return response.status_code, response.text

def test_search_ads():
    """Test failing POST endpoint: search"""
    print("Testing: /sapi/v1/c2c/ads/search")
    
    timestamp = int(time.time() * 1000)
    params = {
        'asset': 'USDT',
        'fiat': 'USD',
        'tradeType': 'BUY',
        'page': 1,
        'rows': 5,
        'timestamp': timestamp
    }
    
    query_string = urlencode(sorted(params.items()))
    signature = generate_signature(SECRET_KEY, query_string)
    params['signature'] = signature
    
    url = f"{BASE_URL}/sapi/v1/c2c/ads/search"
    headers = {
        'X-MBX-APIKEY': API_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.post(url, headers=headers, data=params)
    print(f"Status: {response.status_code}, Response: {response.text}")
    return response.status_code, response.text

def test_get_reference_price():
    """Test failing POST endpoint: getReferencePrice"""
    print("Testing: /sapi/v1/c2c/ads/getReferencePrice")
    
    timestamp = int(time.time() * 1000)
    params = {
        'asset': 'USDT',
        'fiat': 'USD',
        'timestamp': timestamp
    }
    
    query_string = urlencode(sorted(params.items()))
    signature = generate_signature(SECRET_KEY, query_string)
    params['signature'] = signature
    
    url = f"{BASE_URL}/sapi/v1/c2c/ads/getReferencePrice"
    headers = {
        'X-MBX-APIKEY': API_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.post(url, headers=headers, data=params)
    print(f"Status: {response.status_code}, Response: {response.text}")
    return response.status_code, response.text

def test_get_user_order_summary():
    """Test failing GET endpoint: getUserOrderSummary"""
    print("Testing: /sapi/v1/c2c/orderMatch/getUserOrderSummary")
    
    timestamp = int(time.time() * 1000)
    params = {'timestamp': timestamp}
    
    query_string = urlencode(sorted(params.items()))
    signature = generate_signature(SECRET_KEY, query_string)
    url = f"{BASE_URL}/sapi/v1/c2c/orderMatch/getUserOrderSummary?{query_string}&signature={signature}"
    
    headers = {
        'X-MBX-APIKEY': API_KEY,
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    print(f"Status: {response.status_code}, Response: {response.text}")
    return response.status_code, response.text

def test_retrieve_chat_credential():
    """Test failing GET endpoint: retrieveChatCredential"""
    print("Testing: /sapi/v1/c2c/chat/retrieveChatCredential")
    
    timestamp = int(time.time() * 1000)
    params = {'timestamp': timestamp}
    
    query_string = urlencode(sorted(params.items()))
    signature = generate_signature(SECRET_KEY, query_string)
    url = f"{BASE_URL}/sapi/v1/c2c/chat/retrieveChatCredential?{query_string}&signature={signature}"
    
    headers = {
        'X-MBX-APIKEY': API_KEY,
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    print(f"Status: {response.status_code}, Response: {response.text}")
    return response.status_code, response.text

def run_all_tests():
    """Run all failing endpoint tests."""
    if API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Please update API_KEY and SECRET_KEY in the script")
        return
    
    print("Binance P2P API Failing Endpoints Test Suite")
    print("=" * 50)
    print("Expected: All endpoints should return -2008 error")
    print("=" * 50)
    
    failing_count = 0
    total_tests = 5
    
    tests = [
        test_get_available_ads_category,
        test_search_ads,
        test_get_reference_price,
        test_get_user_order_summary,
        test_retrieve_chat_credential
    ]
    
    for i, test_func in enumerate(tests, 1):
        print(f"\n[{i}/{total_tests}] ", end="")
        try:
            status, response = test_func()
            if status == 400 and "-2008" in response:
                print("✅ CONFIRMED: -2008 error as expected")
                failing_count += 1
            else:
                print("❓ UNEXPECTED: Different response than expected")
        except Exception as e:
            print(f"❌ ERROR: {e}")
        
        time.sleep(1)  # Rate limiting
    
    print(f"\n" + "=" * 50)
    print(f"Summary: {failing_count}/{total_tests} endpoints confirmed failing with -2008 error")
    print("This confirms the API key registration bug affecting P2P endpoints")
    print("=" * 50)

if __name__ == "__main__":
    run_all_tests()

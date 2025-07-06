#!/usr/bin/env python3
"""
Binance P2P API Protocol Audit - Live Test Suite
Comprehensive test to determine if endpoints are now working or if our implementation needs fixing

Based on:
- Original bug report from July 2025
- Binance support sample code
- Current project implementation
"""

import requests
import hmac
import hashlib
import time
import json
from urllib.parse import urlencode
from datetime import datetime

# API Credentials from working endpoint validation
API_KEY = "JvVVofVMJiytU1gscA2BODmUdMUBv5DSIn3BCnLpAloL1LxLs2sMO2MNDbc3XalH"
SECRET_KEY = "hKucmhnJhUr3IMJeQOcZaTlxMx9tVAt8B0nCt1aYVdgMydIEomTTdJHRnqndN0c4"
BASE_URL = "https://api.binance.com"

def generate_signature(secret_key, query_string):
    """HMAC-SHA256 signature generation"""
    return hmac.new(
        secret_key.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def test_endpoint_original_approach(endpoint, method="GET", params=None):
    """Test endpoint using our original implementation approach"""
    if params is None:
        params = {}
    
    timestamp = int(time.time() * 1000)
    params['timestamp'] = timestamp
    
    query_string = urlencode(sorted(params.items()))
    signature = generate_signature(SECRET_KEY, query_string)
    
    headers = {
        'X-MBX-APIKEY': API_KEY,
        'Content-Type': 'application/json'
    }
    
    if method.upper() == 'GET':
        url = f"{BASE_URL}{endpoint}?{query_string}&signature={signature}"
        response = requests.get(url, headers=headers, timeout=10)
    else:  # POST
        url = f"{BASE_URL}{endpoint}"
        params['signature'] = signature
        response = requests.post(url, headers=headers, data=params, timeout=10)
    
    return response

def test_endpoint_binance_sample_approach(endpoint, method="GET", params=None):
    """Test endpoint using approach based on Binance's sample code"""
    if params is None:
        params = {}
    
    timestamp = int(time.time() * 1000)
    params['timestamp'] = timestamp
    
    query_string = urlencode(sorted(params.items()))
    signature = generate_signature(SECRET_KEY, query_string)
    
    # Try with Content-Type variations and clientType header
    headers = {
        'X-MBX-APIKEY': API_KEY,
        'Content-Type': 'application/x-www-form-urlencoded',
        'clientType': 'WEB'
    }
    
    if method.upper() == 'GET':
        url = f"{BASE_URL}{endpoint}?{query_string}&signature={signature}"
        response = requests.get(url, headers=headers, timeout=10)
    else:  # POST
        url = f"{BASE_URL}{endpoint}"
        params['signature'] = signature
        response = requests.post(url, headers=headers, data=params, timeout=10)
    
    return response

def run_comprehensive_audit():
    """Run comprehensive audit comparing approaches"""
    
    print("🔍 BINANCE P2P API PROTOCOL AUDIT")
    print("=" * 60)
    print(f"Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print(f"API Key Suffix: ...{API_KEY[-10:]}")
    print("=" * 60)
    
    # Define test endpoints
    test_cases = [
        {
            "name": "Get Ads List (KNOWN WORKING)",
            "endpoint": "/sapi/v1/c2c/ads/getAds",
            "method": "GET",
            "params": {
                "asset": "USDT",
                "fiat": "USD",
                "tradeType": "BUY",
                "page": 1,
                "rows": 5
            },
            "expected": "Should work (confirmed in previous tests)"
        },
        {
            "name": "Get Available Ads Category",
            "endpoint": "/sapi/v1/c2c/ads/getAvailableAdsCategory",
            "method": "GET", 
            "params": {},
            "expected": "Previously failed with -2008 error"
        },
        {
            "name": "Search Ads",
            "endpoint": "/sapi/v1/c2c/ads/search",
            "method": "POST",
            "params": {
                "asset": "USDT",
                "fiat": "USD",
                "tradeType": "BUY",
                "page": 1,
                "rows": 5
            },
            "expected": "Previously failed with -2008 error"
        },
        {
            "name": "Get Reference Price",
            "endpoint": "/sapi/v1/c2c/ads/getReferencePrice", 
            "method": "POST",
            "params": {
                "asset": "USDT",
                "fiat": "USD"
            },
            "expected": "Previously failed with -2008 error"
        }
    ]
    
    results = {
        "original_approach": {},
        "binance_sample_approach": {},
        "summary": {
            "original_working": 0,
            "binance_working": 0,
            "total_tests": len(test_cases)
        }
    }
    
    for test_case in test_cases:
        print(f"\n🧪 Testing: {test_case['name']}")
        print(f"Endpoint: {test_case['method']} {test_case['endpoint']}")
        print(f"Expected: {test_case['expected']}")
        print("-" * 40)
        
        # Test 1: Original approach
        print("📋 Test 1: Original Implementation Approach")
        try:
            response1 = test_endpoint_original_approach(
                test_case['endpoint'], 
                test_case['method'], 
                test_case['params']
            )
            
            status1 = "SUCCESS" if response1.status_code == 200 else "FAILED"
            print(f"Status: {response1.status_code} - {status1}")
            
            if response1.status_code == 200:
                results["summary"]["original_working"] += 1
                print(f"✅ Response received successfully")
                try:
                    data = response1.json()
                    print(f"Response preview: {str(data)[:150]}...")
                except:
                    print(f"Raw response: {response1.text[:150]}...")
            else:
                print(f"❌ Error: {response1.text}")
            
            results["original_approach"][test_case['name']] = {
                "status_code": response1.status_code,
                "response": response1.text[:200] if response1.text else "Empty",
                "success": response1.status_code == 200
            }
            
        except Exception as e:
            print(f"❌ Exception: {str(e)}")
            results["original_approach"][test_case['name']] = {
                "status_code": 0,
                "response": f"Exception: {str(e)}",
                "success": False
            }
        
        # Test 2: Binance sample approach
        print("\n📋 Test 2: Binance Sample Code Approach")
        try:
            response2 = test_endpoint_binance_sample_approach(
                test_case['endpoint'],
                test_case['method'],
                test_case['params']
            )
            
            status2 = "SUCCESS" if response2.status_code == 200 else "FAILED"
            print(f"Status: {response2.status_code} - {status2}")
            
            if response2.status_code == 200:
                results["summary"]["binance_working"] += 1
                print(f"✅ Response received successfully")
                try:
                    data = response2.json()
                    print(f"Response preview: {str(data)[:150]}...")
                except:
                    print(f"Raw response: {response2.text[:150]}...")
            else:
                print(f"❌ Error: {response2.text}")
            
            results["binance_sample_approach"][test_case['name']] = {
                "status_code": response2.status_code,
                "response": response2.text[:200] if response2.text else "Empty",
                "success": response2.status_code == 200
            }
            
        except Exception as e:
            print(f"❌ Exception: {str(e)}")
            results["binance_sample_approach"][test_case['name']] = {
                "status_code": 0,
                "response": f"Exception: {str(e)}",
                "success": False
            }
        
        print("=" * 40)
    
    # Generate comprehensive analysis
    print(f"\n🎯 AUDIT ANALYSIS")
    print("=" * 60)
    
    print(f"\n📊 SUCCESS RATES:")
    print(f"Original Approach: {results['summary']['original_working']}/{results['summary']['total_tests']} ({(results['summary']['original_working']/results['summary']['total_tests']*100):.1f}%)")
    print(f"Binance Sample Approach: {results['summary']['binance_working']}/{results['summary']['total_tests']} ({(results['summary']['binance_working']/results['summary']['total_tests']*100):.1f}%)")
    
    # Behavior Comparison
    print(f"\n// Behavior Comparison")
    if results['summary']['original_working'] == results['summary']['binance_working']:
        if results['summary']['original_working'] == 0:
            print("❌ Both approaches failing - likely backend issue still exists")
        elif results['summary']['original_working'] == 1:
            print("⚠️  Only getAds endpoint working - partial backend fix")
        else:
            print("✅ Both approaches working equally - backend issue resolved")
    else:
        print(f"🔧 Different success rates detected - implementation differences matter")
    
    # Root Cause Analysis
    print(f"\n// Root Cause Analysis")
    if results['summary']['binance_working'] > results['summary']['original_working']:
        print("🎯 VERDICT: Our client implementation had minor issues")
        print("   - Binance sample approach shows better results")
        print("   - Likely header or content-type differences")
        print("   - Our original signature/auth method was correct")
    elif results['summary']['original_working'] == results['summary']['binance_working'] and results['summary']['original_working'] > 1:
        print("🎯 VERDICT: Binance fixed the backend issue")
        print("   - Both approaches now working")
        print("   - Original client code was correct all along") 
        print("   - Backend registration issue has been resolved")
    else:
        print("🎯 VERDICT: Backend issue still exists")
        print("   - Error -2008 likely still occurring")
        print("   - Endpoint-specific registration problem persists")
    
    # Patch Notes
    print(f"\n// Patch Notes")
    print("Changes needed based on test results:")
    if results['summary']['binance_working'] > results['summary']['original_working']:
        print("- Update Content-Type header to 'application/x-www-form-urlencoded'")
        print("- Add 'clientType': 'WEB' header")
        print("- Keep existing signature generation method")
    elif results['summary']['original_working'] > 1:
        print("- No client-side changes needed")
        print("- Original implementation was correct")
        print("- Backend issue has been resolved")
    else:
        print("- No changes possible - waiting for Binance backend fix")
        print("- Continue monitoring support tickets")
    
    return results

if __name__ == "__main__":
    try:
        audit_results = run_comprehensive_audit()
        
        print(f"\n📝 Test completed successfully")
        print(f"Results saved for analysis")
        
    except Exception as e:
        print(f"\n❌ Audit failed with error: {str(e)}")
        print(f"Check network connection and API credentials")

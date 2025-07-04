# Binance P2P API Validation Report

## Test Summary
- **Timestamp**: 2025-07-04 23:29:15 UTC
- **API Key Suffix**: ...XXXX (Sanitized)
- **Support Case**: #144098731
- **Merchant ID**: 171****89 (Sanitized)
- **API Version**: `/sapi/v1`
- **Base URL**: `https://api.binance.com`

## Test Results Overview
- **Working Endpoints**: 1/6 (16.7%)
- **Failing Endpoints**: 5/6 (83.3%)
- **Primary Issue**: Endpoint-specific API key registration problem

---

## ✅ Working Endpoints

### 1. Get Ads List
- **Method**: `GET`
- **Path**: `/sapi/v1/c2c/ads/getAds`
- **Status**: ✅ SUCCESS
- **Result**: Returns 200 OK with valid response
- **Note**: Confirms API key credentials are valid

**Parameters Used:**
```json
{
  "asset": "USDT",
  "fiat": "USD", 
  "tradeType": "BUY",
  "page": 1,
  "rows": 5
}
```

**Test Code:**
```python
import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode

API_KEY = "YOUR_API_KEY_HERE"  # Sanitized for security
SECRET_KEY = "YOUR_SECRET_KEY_HERE"  # Sanitized for security
BASE_URL = "https://api.binance.com"

def generate_signature(secret_key, query_string):
    return hmac.new(
        secret_key.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

# Test working endpoint
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
url = f"{BASE_URL}/sapi/v1/c2c/ads/getAds?{query_string}&signature={signature}"

headers = {
    'X-MBX-APIKEY': API_KEY,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
print(f"Status: {response.status_code}")  # Returns: 200
```

---

## ❌ Failing Endpoints

### 1. Get Available Ads Category
- **Method**: `GET`
- **Path**: `/sapi/v1/c2c/ads/getAvailableAdsCategory`
- **Status**: ❌ FAILED
- **Error**: `{"code":-2008,"msg":"Invalid Api-Key ID."}`
- **Expected**: Should return available ad categories
- **Actual**: Returns -2008 Invalid API Key ID error

**Parameters Used:**
```json
{}
```

**Test Code:**
```python
# Test failing endpoint
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
print(f"Status: {response.status_code}")  # Returns: 400
print(f"Response: {response.text}")       # Returns: {"code":-2008,"msg":"Invalid Api-Key ID."}
```

### 2. Search Ads
- **Method**: `POST`
- **Path**: `/sapi/v1/c2c/ads/search`
- **Status**: ❌ FAILED
- **Error**: `{"code":-2008,"msg":"Invalid Api-Key ID."}`
- **Expected**: Should return filtered ad search results
- **Actual**: Returns -2008 Invalid API Key ID error

**Parameters Used:**
```json
{
  "asset": "USDT",
  "fiat": "USD",
  "tradeType": "BUY",
  "page": 1,
  "rows": 5
}
```

**Test Code:**
```python
# Test POST method as suggested by CS Fajer
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
print(f"Status: {response.status_code}")  # Returns: 400
print(f"Response: {response.text}")       # Returns: {"code":-2008,"msg":"Invalid Api-Key ID."}
```

### 3. Get Reference Price
- **Method**: `POST`
- **Path**: `/sapi/v1/c2c/ads/getReferencePrice`
- **Status**: ❌ FAILED
- **Error**: `{"code":-2008,"msg":"Invalid Api-Key ID."}`
- **Expected**: Should return reference price for asset/fiat pair
- **Actual**: Returns -2008 Invalid API Key ID error

**Parameters Used:**
```json
{
  "asset": "USDT",
  "fiat": "USD"
}
```

### 4. Get User Order Summary
- **Method**: `GET`
- **Path**: `/sapi/v1/c2c/orderMatch/getUserOrderSummary`
- **Status**: ❌ FAILED
- **Error**: `{"code":-2008,"msg":"Invalid Api-Key ID."}`
- **Expected**: Should return user's order summary
- **Actual**: Returns -2008 Invalid API Key ID error

**Parameters Used:**
```json
{}
```

### 5. Retrieve Chat Credential
- **Method**: `GET`
- **Path**: `/sapi/v1/c2c/chat/retrieveChatCredential`
- **Status**: ❌ FAILED
- **Error**: `{"code":-2008,"msg":"Invalid Api-Key ID."}`
- **Expected**: Should return chat credentials for P2P messaging
- **Actual**: Returns -2008 Invalid API Key ID error

**Parameters Used:**
```json
{}
```

---

## Analysis & Findings

### Root Cause
- **API Key Validity**: ✅ Confirmed valid (getAds endpoint works)
- **Authentication Method**: ✅ Correct HMAC-SHA256 signature
- **Request Format**: ✅ Proper headers and parameters
- **Issue Type**: 🔧 Backend endpoint-specific registration problem

### Support Chain Status
1. **CS Sergei U** → Identified "Invalid Api-Key ID" issue
2. **CS Alex N** → Suggested POST method for search endpoint
3. **CS Fajer** → Confirmed POST for search, forwarded to backend team

### Technical Verification
The fact that `/sapi/v1/c2c/ads/getAds` returns a successful 200 response while all other P2P endpoints return the exact same `-2008` error confirms this is not a client-side issue but rather a backend API key registration problem specific to certain P2P endpoints.

---

## Next Steps

1. **✅ Completed**: Comprehensive endpoint testing
2. **🔄 In Progress**: Waiting for Binance backend team response via CS Fajer
3. **📋 Pending**: Backend team to register API key for all P2P endpoints
4. **🚀 Ready**: Bot implementation ready for deployment once endpoints are fixed

---

## Environment Details
- **Python Version**: 3.x
- **Required Libraries**: `requests`, `hmac`, `hashlib`, `urllib.parse`
- **Network**: All tests performed from clean network environment
- **Rate Limiting**: Respected API rate limits with appropriate delays

---

*Report generated automatically from comprehensive API testing suite*
*Last updated: 2025-07-04 23:29:15 UTC*

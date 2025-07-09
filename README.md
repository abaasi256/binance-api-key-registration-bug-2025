# Binance P2P API Key Registration Bug - Case #144098731

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Backend Fix In Progress](https://img.shields.io/badge/Status-Backend%20Fix%20In%20Progress-orange.svg)](https://github.com)
[![Binance Support](https://img.shields.io/badge/Binance%20Support-Case%20%23144098731-blue.svg)](https://github.com)
[![Progress: 50%](https://img.shields.io/badge/Progress-50%25%20Endpoints%20Working-yellow.svg)](https://github.com)

> **Complete documentation of Binance P2P API key registration issue and resolution process**

## 🚨 **Issue Summary**

This repository documents a critical **Binance P2P API key registration bug** where valid API credentials fail on specific P2P endpoints with `-2008 Invalid Api-Key ID` error, despite working correctly on other endpoints.

### **🎯 Latest Update - July 9, 2025**
- **Progress:** 3/6 endpoints now working (50% success rate, up from 16.7%)
- **Backend Changes:** Binance team actively deploying fixes - endpoints fluctuating between working/failing
- **Support Escalation:** CS Sergei U (Merchant Team) now handling case with technical expertise
- **Evidence:** Multiple API key generations show backend modifications in progress

### **Key Facts**
- **Issue Type:** Backend API key registration problem (Binance-side)
- **Current Status:** Backend fix deployment in progress (confirmed by endpoint fluctuations)
- **Working Endpoints:** `/getAds`, `/getUserOrderSummary`, `/getAvailableAdsCategory` (intermittent)
- **Support Case:** #144098731 (escalated to Merchant Team)
- **Timeline:** Active backend development confirmed July 9, 2025

---

## 📋 **Repository Contents**

### **📄 Core Documentation**
- **[Support Timeline](docs/binance_support_timeline.md)** - Complete case history including CS Sergei escalation
- **[Backend Progress Evidence](docs/backend_progress_evidence.md)** - July 9, 2025 fluctuation documentation
- **[API Validation Report](docs/binance_api_validation.md)** - Detailed testing results
- **[Audit Results](audits/binance-backend-2025/)** - Comprehensive endpoint testing

### **🧪 Test Scripts**
- **[Failing Endpoints Test](test/test_failing_endpoints.py)** - Demonstrates the bug
- **[Working Endpoint Test](test/test_working_endpoint.py)** - Proves credentials work
- **[Requirements](test/requirements.txt)** - Python dependencies

### **📚 Reference Materials**
- **[Original Binance Guides](Original_Binance_Guides/)** - Official documentation from support
- **[Security Policy](SECURITY.md)** - Responsible disclosure information
- **[Contributing Guidelines](CONTRIBUTING.md)** - How to contribute

---

## 🔍 **The Issue Explained**

### **What's Happening**
```bash
# This works ✅
curl -X GET "https://api.binance.com/sapi/v1/c2c/ads/getAds?..."
# Returns: 200 OK with valid data

# This fails ❌
curl -X POST "https://api.binance.com/sapi/v1/c2c/ads/search?..."
# Returns: {"code":-2008,"msg":"Invalid Api-Key ID."}
```

### **Why It's a Backend Issue**
1. **Same API Key:** Both requests use identical credentials
2. **Correct Format:** Request structure follows Binance documentation exactly
3. **Selective Failure:** Only affects specific P2P endpoints
4. **Consistent Pattern:** Multiple merchants report identical issue

---

## 🛠️ **Technical Details**

### **Correct Request Format** *(Confirmed by Binance Support)*
```bash
curl --location 'https://api.binance.com/sapi/v1/c2c/ads/search?recvWindow=5000&timestamp={timestamp}&signature={signature}' \
--header 'X-MBX-APIKEY: {api_key}' \
--header 'Content-Type: application/json' \
--data '{
    "asset": "USDT",
    "fiat": "USD",
    "page": 1,
    "rows": 10,
    "tradeType": "BUY"
}'
```

### **Key Implementation Points**
- **Signature Scope:** Only `recvWindow`, `timestamp` in query string
- **Body Parameters:** All trading parameters in JSON body
- **Headers:** `X-MBX-APIKEY` and `Content-Type: application/json`
- **Algorithm:** HMAC-SHA256 from query string only

---

## 🧪 **Reproduction Steps**

### **Prerequisites**
```bash
pip install -r test/requirements.txt
```

### **Run Tests**
```bash
# Test the working endpoint (should succeed)
python test/test_working_endpoint.py

# Test the failing endpoints (will show -2008 error)
python test/test_failing_endpoints.py
```

### **Expected Results**
- **Working endpoint:** Returns marketplace data ✅
- **Failing endpoints:** Return `-2008 Invalid Api-Key ID` ❌

---

## 📊 **Impact Analysis**

### **Impact Analysis**

| Feature | Status | Latest Change |
|---------|--------|---------------|
| **Get Ads List** | ✅ Working | Consistently stable |
| **Get User Order Summary** | ✅ Working | Recently activated |
| **Get Available Ads Category** | 🔄 Intermittent | Backend deployment in progress |
| **Search Ads** | ❌ Failing | Awaiting backend fix |
| **Reference Prices** | ❌ Failing | Awaiting backend fix |
| **Chat Credentials** | ❌ Failing | Parameter configuration needed |

### **Progress Timeline**
- **July 5-6:** 1/6 endpoints working (16.7%)
- **July 9 AM:** 3/6 endpoints working (50%) 
- **July 9 PM:** Fluctuating between 1-3 endpoints (backend changes active)
- **Current:** Backend team actively deploying fixes

### **Business Impact**
- **Automated Trading:** Severely limited functionality
- **Market Analysis:** Cannot access filtered data
- **Price Discovery:** No reference price capabilities
- **Bot Development:** Blocked advanced features

---

## 📞 **Support Status**

### **Binance Support Case #144098731**
- **Status:** 🔄 Backend team actively deploying fixes
- **Current Handler:** CS Sergei U (Merchant Team) - Technical specialist
- **Priority:** HIGH (production blocking)
- **Evidence:** Endpoint fluctuations confirm backend development in progress
- **Latest:** July 9, 2025 - Multiple API key tests show active backend changes

### **What Binance Needs to Do**
1. **Enable P2P API access** for affected API keys
2. **Verify backend registration** in P2P systems
3. **Remove access restrictions** blocking specific endpoints
4. **Test and confirm** full functionality restored

---

## 🤝 **Contributing**

### **How to Help**
- **Reproduce the issue** using your own Binance API credentials
- **Share testing results** in GitHub Issues
- **Document workarounds** or partial solutions
- **Update status** when Binance resolves the issue

### **Testing Guidelines**
1. **Never expose real API keys** in public repositories
2. **Use placeholder credentials** in code examples
3. **Document your testing environment** for reference
4. **Report new findings** through GitHub Issues

---

## 🔒 **Security Notice**

### **Credential Safety**
- ✅ **No real API keys** exposed in this repository
- ✅ **All sensitive data** properly sanitized
- ✅ **Safe for public sharing** and collaboration

### **Testing Safety**
- **Use testnet credentials** when possible
- **Mask production keys** in logs and screenshots
- **Follow responsible disclosure** for security issues

---

## 📈 **Resolution Timeline**

### **Current Phase: Backend Deployment Active**
```
[✅] Issue Discovery & Documentation
[✅] Binance Support Engagement  
[✅] Format Verification & Implementation
[✅] Backend Team Escalation
[🔄] Backend Fix Deployment ← WE ARE HERE
[⏸️] Final Testing & Validation
[⏸️] Production Completion
```

### **Evidence of Active Development**
- **Endpoint Fluctuations:** Same endpoints switching between working/failing over hours
- **Success Rate Changes:** 16.7% → 50% → 16.7% within single day
- **Error Pattern Evolution:** Moving from consistent -2008 to mixed error types
- **Support Escalation:** Merchant Team (CS Sergei) now handling case

---

## 📚 **Additional Resources**

### **Official Documentation**
- [Binance P2P API Documentation](https://binance-docs.github.io/apidocs/spot/en/#c2c-endpoints)
- [API Authentication Guide](https://binance-docs.github.io/apidocs/spot/en/#signed-trade-and-user_data-endpoint-security)

### **Community Resources**
- [GitHub Issues](../../issues) - Latest updates and discussions
- [Support Timeline](docs/binance_support_timeline.md) - Complete case documentation

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ **Star This Repository**

If this documentation helped you understand or resolve similar Binance API issues, please star this repository to help others find it!

---

**📧 Questions?** Open a [GitHub Issue](../../issues/new) or check our [Contributing Guidelines](CONTRIBUTING.md).

**🔔 Updates:** Watch this repository for notifications when the issue is resolved.

**🐛 Similar Issues?** Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) to document your experience.

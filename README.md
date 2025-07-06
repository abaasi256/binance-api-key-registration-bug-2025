# Binance P2P API Key Registration Bug - Case #144098731

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Backend Fix Required](https://img.shields.io/badge/Status-Backend%20Fix%20Required-red.svg)](https://github.com)
[![Binance Support](https://img.shields.io/badge/Binance%20Support-Case%20%23144098731-blue.svg)](https://github.com)

> **Complete documentation of Binance P2P API key registration issue and resolution process**

## 🚨 **Issue Summary**

This repository documents a critical **Binance P2P API key registration bug** where valid API credentials fail on specific P2P endpoints with `-2008 Invalid Api-Key ID` error, despite working correctly on other endpoints.

### **Key Facts**
- **Issue Type:** Backend API key registration problem (Binance-side)
- **Affected Endpoints:** `/sapi/v1/c2c/ads/search`, `/sapi/v1/c2c/ads/getReferencePrice`, and others
- **Working Endpoints:** `/sapi/v1/c2c/ads/getAds` (proves credentials are valid)
- **Support Case:** #144098731
- **Status:** Awaiting Binance backend team resolution

---

## 📋 **Repository Contents**

### **📄 Core Documentation**
- **[Support Timeline](docs/binance_support_timeline.md)** - Complete case history and technical analysis
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

### **Affected Functionality**
| Feature | Status | Impact |
|---------|--------|--------|
| **Get Ads List** | ✅ Working | Basic marketplace access |
| **Search Ads** | ❌ Failing | Cannot filter/search marketplace |
| **Reference Prices** | ❌ Failing | No price benchmarking |
| **Ad Categories** | ❌ Failing | Limited market analysis |

### **Business Impact**
- **Automated Trading:** Severely limited functionality
- **Market Analysis:** Cannot access filtered data
- **Price Discovery:** No reference price capabilities
- **Bot Development:** Blocked advanced features

---

## 📞 **Support Status**

### **Binance Support Case #144098731**
- **Status:** ⏳ Awaiting backend team resolution
- **Priority:** HIGH (production blocking)
- **Evidence:** Complete technical documentation provided
- **Next Steps:** Backend API key registration fix required

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

### **Current Phase: Awaiting Backend Fix**
```
[✅] Issue Discovery & Documentation
[✅] Binance Support Engagement  
[✅] Format Verification & Implementation
[⏳] Backend Team Resolution ← WE ARE HERE
[⏸️] Testing & Validation
[⏸️] Production Deployment
```

### **Expected Resolution**
When Binance fixes the backend registration issue:
1. **Immediate activation** - No code changes required
2. **Full functionality** - All P2P endpoints accessible
3. **Production ready** - Complete implementation already done

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

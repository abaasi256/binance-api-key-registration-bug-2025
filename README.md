# Binance API Key Registration Bug Report - 2025

![GitHub Repo](https://img.shields.io/badge/Repository-binance--api--key--registration--bug--2025-blue)
![Bug Status](https://img.shields.io/badge/Status-Under%20Investigation-orange)
![Binance Case](https://img.shields.io/badge/Support%20Case-%23144098731-red)
![API Endpoints](https://img.shields.io/badge/Affected%20Endpoints-5%2F6-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Documentation](https://img.shields.io/badge/Documentation-Complete-brightgreen)

**Discovery Date:** July 3, 2025  
**Reporter:** Security Research Team  
**Status:** Under Investigation by Binance Backend Team  
**Support Case:** #144098731  

## Bug Summary

A critical inconsistency has been discovered in Binance's `/sapi/v1/c2c/` endpoint behavior where a valid API key works on some endpoints but fails with error `-2008 "Invalid Api-Key ID"` on others.

**Impact:** Prevents developers from accessing essential P2P trading functionality despite having valid, authenticated API credentials.

## Quick Facts

- **Working Endpoints:** 1/6 tested (16.7% success rate)
- **Failing Endpoints:** 5/6 tested (83.3% failure rate)  
- **Error Pattern:** Consistent `-2008` error across failing endpoints
- **Root Cause:** Backend API key registration inconsistency

## Affected Endpoints

### ✅ Working
- `GET /sapi/v1/c2c/ads/getAds` - Returns 200 OK

### ❌ Failing (Error -2008)
- `GET /sapi/v1/c2c/ads/getAvailableAdsCategory`
- `POST /sapi/v1/c2c/ads/search`
- `POST /sapi/v1/c2c/ads/getReferencePrice`
- `GET /sapi/v1/c2c/orderMatch/getUserOrderSummary`
- `GET /sapi/v1/c2c/chat/retrieveChatCredential`

## Reproduction Steps

1. Generate valid Binance API key with P2P trading permissions
2. Test `getAds` endpoint → **Success (200 OK)**
3. Test any other P2P endpoint → **Failure (-2008)**
4. Verify same credentials, signature method, headers across all tests

## Technical Details

The bug is confirmed to be server-side because:
- Same API key works on one endpoint but fails on others
- Identical authentication method (HMAC-SHA256) used across all tests
- Consistent error pattern suggests backend registration issue
- Multiple Binance support agents have escalated to backend team

## Repository Structure

```
├── README.md                    # This file
├── DISCLOSURE.md               # Timeline and disclosure process
├── LICENSE                     # MIT License
├── .gitignore                 # Python gitignore
├── docs/
│   └── binance_api_validation.md    # Detailed technical report
└── test/
    ├── test_working_endpoint.py     # Test for working getAds endpoint
    ├── test_failing_endpoints.py    # Test suite for failing endpoints
    └── requirements.txt             # Python dependencies
```

## Documentation

- **[Complete Technical Report](docs/binance_api_validation.md)** - Detailed analysis with code examples
- **[Disclosure Timeline](DISCLOSURE.md)** - Responsible disclosure process

**Note:** PDF report excluded from repository due to sensitive information.

## Test Code

Ready-to-run Python test scripts are available in the `/test` directory to reproduce this issue.

## Disclaimer

This repository is for **transparency and developer awareness** only. We are working with Binance through official channels to resolve this issue. This is not a security vulnerability but rather a system inconsistency that affects legitimate API usage.

## Current Status

- **Reported:** July 3, 2025 (Support Case #144098731)
- **Escalated:** To Binance Backend Team via CS Fajer
- **HackerOne Access:** Requested for formal bug bounty submission
- **Resolution:** Pending backend team investigation

## Contact

For technical questions about reproduction steps or additional test cases, please open an issue in this repository.

---

**⚠️ Important:** This bug affects legitimate API usage and should be resolved to ensure consistent developer experience across Binance's P2P trading API endpoints.

---
name: Bug Report
about: Report a similar API key registration issue
title: '[BUG] Endpoint experiencing -2008 error'
labels: ['bug', 'api-error', 'needs-verification']
assignees: ''

---

## Describe the Bug
A clear description of the API endpoint experiencing the -2008 "Invalid Api-Key ID" error.

## Affected Endpoint
- **Method**: GET/POST
- **Path**: `/sapi/v1/...`
- **Expected**: Working endpoint
- **Actual**: -2008 error

## Reproduction Steps
1. Create valid Binance API key with appropriate permissions
2. Test endpoint with proper HMAC-SHA256 signature
3. Receive -2008 error

## Environment
- **API Key Type**: [Spot/Futures/P2P]
- **Permissions**: [List permissions enabled]
- **Testing Method**: [Python/cURL/Other]
- **IP Restrictions**: [Yes/No]

## Additional Context
- [ ] Confirmed API key works on other endpoints
- [ ] Verified signature generation method
- [ ] Tested with fresh API key
- [ ] Contacted Binance support (case #: ______)

## Error Response
```json
{"code":-2008,"msg":"Invalid Api-Key ID."}
```

---
**Note**: This repository documents the systematic -2008 error affecting multiple P2P endpoints. Please include relevant technical details to help build a comprehensive issue catalog.

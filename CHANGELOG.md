# Changelog

## [1.1.0] - 2025-07-09

### Changed
- **MAJOR PROGRESS**: Backend fix deployment confirmed active
- **Success Rate**: Improved from 16.7% (1/6) to 50% (3/6) endpoints working
- **Support Escalation**: CS Sergei U (Merchant Team) took over case from CS Lily

### Added
- Backend progress evidence documentation
- Multiple API key generation testing (3 fresh keys)
- Endpoint fluctuation behavior documentation
- Technical support interaction logs with CS Sergei

### Fixed
- `/sapi/v1/c2c/orderMatch/getUserOrderSummary` - Now working consistently
- `/sapi/v1/c2c/ads/getAvailableAdsCategory` - Intermittently working (backend deployment)

### Backend Evidence
- **Fluctuating Endpoints**: Same endpoints switching between working/failing
- **Error Evolution**: From consistent -2008 to mixed error types (-1022, 500)
- **Active Development**: Fresh API keys show backend team deploying changes
- **Timeline**: Multiple tests within hours showing different success rates

### Support Updates
- CS Lily initially misdiagnosed as "no backend issue"
- CS Sergei U (Merchant Team) demonstrates technical competence
- Backend team confirmed actively working on endpoint registration
- Case priority elevated due to technical evidence provided

## [1.0.0] - 2025-07-05

### Added
- Initial repository creation for Binance API key registration bug documentation
- Comprehensive README.md with bug summary and reproduction steps
- Detailed technical report in `/docs/binance_api_validation.md`
- PDF report copy in `/docs/binance_api_validation.pdf`
- Test scripts for working and failing endpoints in `/test/` directory
- Responsible disclosure timeline in `DISCLOSURE.md`
- MIT license
- Python gitignore configuration

### Security
- Sanitized all API keys and sensitive information from public documentation
- Replaced actual API keys with placeholder values in test scripts
- Masked merchant ID showing only partial digits (171****89) for privacy protection

### Documentation
- Documented 6 P2P endpoints with 1 working, 5 failing
- Confirmed -2008 "Invalid Api-Key ID" error pattern
- Included support case #144098731 reference
- Added reproduction steps and technical analysis

---

*This changelog follows [Keep a Changelog](https://keepachangelog.com/) format.*

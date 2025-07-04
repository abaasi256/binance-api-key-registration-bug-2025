# Changelog

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

### Documentation
- Documented 6 P2P endpoints with 1 working, 5 failing
- Confirmed -2008 "Invalid Api-Key ID" error pattern
- Included support case #144098731 reference
- Added reproduction steps and technical analysis

---

*This changelog follows [Keep a Changelog](https://keepachangelog.com/) format.*

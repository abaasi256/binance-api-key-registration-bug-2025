# Responsible Disclosure Timeline

## Bug Discovery & Reporting Process

### Discovery Phase
- **July 3, 2025**: Initial discovery during P2P bot development
- **July 3, 2025**: Comprehensive endpoint testing confirms inconsistent behavior
- **July 3, 2025**: API key validation confirms credentials are working on some endpoints

### Official Reporting
- **July 3, 2025**: Submitted to Binance Customer Support
  - **Case Number**: #144098731
  - **Initial Contact**: CS Sergei U
  - **Issue**: "Invalid Api-Key ID" error on specific P2P endpoints

### Support Chain Escalation
- **July 3, 2025**: CS Alex N suggests POST method for search endpoint
- **July 3, 2025**: CS Fajer confirms POST testing and escalates to backend team
- **July 4, 2025**: Comprehensive testing report compiled and shared
- **July 5, 2025**: Public documentation created for developer awareness

### HackerOne Submission
- **July 5, 2025**: Requested HackerOne access for formal bug bounty submission
- **Status**: Pending access approval
- **Classification**: System inconsistency affecting legitimate API usage

## Communication Channels

### Primary Channel
- **Binance Customer Support**
- **Case #144098731**
- **Current Handler**: CS Fajer (Backend Team Liaison)

### Secondary Channel
- **HackerOne Bug Bounty Program**
- **Status**: Access requested
- **Purpose**: Formal vulnerability disclosure

### Public Documentation
- **GitHub Repository**: For developer transparency
- **Purpose**: Warn other developers, provide reproduction steps
- **Scope**: Technical documentation only, no exploit details

## Resolution Timeline

### Immediate Actions (Completed)
- ✅ Comprehensive endpoint testing
- ✅ Documentation of affected endpoints
- ✅ Proof-of-concept test code
- ✅ Support case submission
- ✅ Backend team escalation

### Pending Actions
- 🔄 Backend team investigation
- 🔄 HackerOne access approval
- 🔄 API key registration fix deployment
- 🔄 Resolution confirmation testing

### Post-Resolution
- 📋 Update documentation with fix details
- 📋 Confirm all endpoints working
- 📋 Archive repository with resolution status

## Contact Information

For questions about this disclosure process:
- **Support Reference**: Case #144098731
- **Technical Questions**: Open GitHub issue in this repository
- **Security Concerns**: Contact through official Binance security channels

---

**Note**: This disclosure follows responsible security research practices. The issue has been reported through official channels before any public documentation.

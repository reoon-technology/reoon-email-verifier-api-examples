# Reoon Email Verifier API - Code Examples

Official code examples for integrating Reoon Email Verifier API into your applications. Verify email addresses with high accuracy using our powerful email verification service.

## 🚀 About Reoon Email Verifier

[Reoon Email Verifier](https://www.reoon.com/email-verifier/) is a professional email verification service that helps you validate email addresses in real-time. Clean your email lists, reduce bounce rates, and improve email deliverability with our advanced verification technology.

### Key Features

- **Single Email Verification** - Verify emails instantly with Quick or Power mode  
- **Bulk Email Verification** - Process up to 50,000 emails at once  
- **Disposable Email Detection** - Identify temporary/disposable email addresses  
- **Syntax Validation** - Check email format and structure  
- **MX Record Verification** - Validate domain and mail server configuration  
- **SMTP Verification** - Deep inbox-level verification (Power mode)  
- **Catch-All Detection** - Identify catch-all domains  
- **Role Account Detection** - Flag role-based emails (info@, support@, etc.)  
- **Free Email Detection** - Identify free email providers  
- **Spam Trap Detection** - Protect your sender reputation

## 📚 Available Examples

### Python
- **[single_verify.py](python/single_verify.py)** - Single email verification (Quick & Power mode)
- **[bulk_verify.py](python/bulk_verify.py)** - Bulk email verification with progress tracking

### Coming Soon
- JavaScript/Node.js
- PHP
- Java
- C#/.NET

## 🔑 Getting Your API Key

To use these examples, you need a Reoon API key:

1. Create Your **[Email Verifier](https://emailverifier.reoon.com/register/)** Account - Get up to 600 credits/month free
2. Generate your API key from the dashboard
3. Replace `your_api_key_here` in the example code with your actual key

## 💻 Python Examples

### Installation

```bash
pip install requests
```

### Single Email Verification

```python
from single_verify import reoon_verify_quick, reoon_verify_power

# Quick Mode (fast, ~0.5 seconds)
result = reoon_verify_quick("test@example.com", "your_api_key")
print(result)

# Power Mode (deep verification, checks inbox)
result = reoon_verify_power("test@example.com", "your_api_key")
print(result)
```

### Bulk Email Verification

```python
from bulk_verify import reoon_bulk_verify_and_wait

emails = ["email1@example.com", "email2@example.com", "email3@example.com"]

# Create task and wait for completion
results = reoon_bulk_verify_and_wait(emails, "your_api_key", "My Task")

# Access individual results
for email, data in results['results'].items():
    print(f"{email}: {data['status']}")
```

## 📖 Verification Modes

### Quick Mode
- ⚡ Ultra-fast verification (~0.5 seconds)
- ✅ Perfect for real-time validation during user registration
- ⚠️ Does NOT check individual inbox existence
- Checks: Syntax, disposable, MX records, domain acceptance

### Power Mode
- 🔍 Deep verification with inbox-level checks
- ✅ Most accurate verification available
- ⏱️ Takes a few seconds (depends on email provider)
- Checks: Everything in Quick mode + inbox existence, catch-all, deliverability

## 📊 API Response Status

### Single Verification
**Quick Mode:** `valid`, `invalid`, `disposable`, `spamtrap`  
**Power Mode:** `safe`, `invalid`, `disabled`, `disposable`, `inbox_full`, `catch_all`, `role_account`, `spamtrap`, `unknown`

### Bulk Verification
All emails are verified using **Power Mode** for maximum accuracy.

## 🔗 API Documentation

For complete API documentation, visit: [Reoon Email Verifier API Docs](https://www.reoon.com/articles/api-documentation-of-reoon-email-verifier/)

## 💡 Use Cases

- **User Registration** - Prevent fake signups with disposable emails
- **Email List Cleaning** - Remove invalid emails before campaigns
- **CRM Integration** - Validate emails at point of entry
- **Marketing Automation** - Improve email deliverability
- **Lead Verification** - Ensure lead quality and accuracy
- **E-commerce** - Validate customer emails during checkout

## ⚙️ Rate Limits & Credits

- **Single Verification API:** Do not use more than 5 concurrent threads
- **Bulk Verification API:** Up to 50,000 emails per task
- **Free Plan:** Up to 600 credits/month
- **Paid Plans:** Available for higher volumes


## 🛠️ Integration Support

Need help integrating Reoon Email Verifier into your application?

- 📧 **Support:** Contact via [Reoon Customer Support](https://www.reoon.com/contact-support/)
- 📚 **Documentation:** [Reoon API Documentation](https://www.reoon.com/articles/api-documentation-of-reoon-email-verifier/)

## 📄 License

These examples are provided as-is for use with the [Reoon Email Verifier service](https://www.reoon.com/email-verifier/). Feel free to modify and use them in your projects.

## 🌟 Why Choose Reoon Email Verifier?

- ✅ High accuracy verification with advanced SMTP checks
- ✅ Fast API response times
- ✅ Generous free tier (600 credits/month)
- ✅ No credit card required to start
- ✅ Bulk verification support
- ✅ Detailed verification results
- ✅ Easy integration with any programming language
- ✅ Excellent customer support

## 🚀 Get Started Now

Ready to clean your email lists and improve deliverability?

**[Create Reoon Email Verifier Account](https://emailverifier.reoon.com/register/)**

No credit card required. Get 600 free credits per month.

---

**Made with ❤️ by [Reoon Technology](https://www.reoon.com/)**

*Improve your email deliverability with professional email verification.*

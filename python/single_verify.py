import requests
import json

def reoon_verify_quick(email, api_key):
    """
    Verify email using Reoon Quick Mode (fast, ~0.5 seconds)
    Note: Quick mode does NOT check individual inbox status
    """
    url = f"https://emailverifier.reoon.com/api/v1/verify?email={email}&key={api_key}&mode=quick"
    
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}


def reoon_verify_power(email, api_key):
    """
    Verify email using Reoon Power Mode (deep verification, checks inbox)
    Note: This can take several seconds to complete
    """
    url = f"https://emailverifier.reoon.com/api/v1/verify?email={email}&key={api_key}&mode=power"
    
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    # Replace with your actual API key from https://emailverifier.reoon.com/register/
    API_KEY = "your_api_key_here"
    EMAIL = "test@example.com"
    
    # Quick Mode Verification
    print("Quick Mode Verification:")
    print("-" * 50)
    result = reoon_verify_quick(EMAIL, API_KEY)
    print(json.dumps(result, indent=2))
    
    print("\n" + "=" * 50 + "\n")
    
    # Power Mode Verification
    print("Power Mode Verification:")
    print("-" * 50)
    result = reoon_verify_power(EMAIL, API_KEY)
    print(json.dumps(result, indent=2))
  

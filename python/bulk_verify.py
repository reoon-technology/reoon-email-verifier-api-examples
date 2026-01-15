import requests
import json
import time

def reoon_bulk_verify(emails, api_key, task_name="Bulk Verification"):
    """
    Create bulk email verification task with Reoon
    Returns: task_id if successful, or error details
    """
    url = "https://emailverifier.reoon.com/api/v1/create-bulk-verification-task/"
    
    payload = {
        "name": task_name,
        "emails": emails,
        "key": api_key
    }
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 201:
            return response.json()
        else:
            return {"error": response.json()}
    except Exception as e:
        return {"error": str(e)}


def reoon_get_bulk_results(task_id, api_key):
    """
    Get results of bulk verification task from Reoon
    Returns: task status and results (if completed)
    """
    url = f"https://emailverifier.reoon.com/api/v1/get-result-bulk-verification-task/?key={api_key}&task_id={task_id}"
    
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}


def reoon_bulk_verify_and_wait(emails, api_key, task_name="Bulk Verification", check_interval=5):
    """
    Create task and wait for completion (polls every check_interval seconds)
    Returns: final results when task is completed
    """
    # Step 1: Create task
    print("Creating bulk verification task...")
    task_response = reoon_bulk_verify(emails, api_key, task_name)
    
    if "error" in task_response:
        return task_response
    
    task_id = task_response.get("task_id")
    print(f"Task created successfully! Task ID: {task_id}")
    print(f"Processing {task_response.get('count_processing')} emails...\n")
    
    # Step 2: Poll for results
    while True:
        result = reoon_get_bulk_results(task_id, api_key)
        
        status = result.get("status")
        progress = result.get("progress_percentage", 0)
        
        print(f"Status: {status} | Progress: {progress}%")
        
        if status == "completed":
            print("\nVerification completed!")
            return result
        elif status == "error":
            print("\nTask failed!")
            return result
        
        time.sleep(check_interval)


if __name__ == "__main__":
    # Replace with your actual API key from https://emailverifier.reoon.com/register/
    API_KEY = "your_api_key_here"
    
    # List of emails to verify
    emails_to_verify = [
        "test1@example.com",
        "test2@example.com",
        "test3@example.com",
        "john@gmail.com",
        "jane@yahoo.com"
    ]
    
    # Option 1: Create task and get task_id only
    print("=" * 60)
    print("Option 1: Create Task Only")
    print("=" * 60)
    task_response = reoon_bulk_verify(emails_to_verify, API_KEY, "My Task")
    print(json.dumps(task_response, indent=2))
    
    # Option 2: Create task and wait for completion
    print("\n" + "=" * 60)
    print("Option 2: Create Task and Wait for Results")
    print("=" * 60)
    final_results = reoon_bulk_verify_and_wait(emails_to_verify, API_KEY, "My Task")
    
    # Print specific email results
    if final_results.get("status") == "completed":
        results = final_results.get("results", {})
        for email, data in results.items():
            print(f"\n{email}: {data.get('status')}")
          

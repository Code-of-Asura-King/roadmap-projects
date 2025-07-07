import json
import sys
import requests


def get_user_activity(username):
    url=f"https://api.github.com/users/{username}/events"
    
    try:
        response=requests.get(url)
        print(response.status_code)
        
        if (response.status_code==200):
            
            events = response.json()
            if not events:
                print("No recent activity found.")
                return

            for event in events:
                type = event["type"]
                repo_name = event["repo"]["name"]

                if type == "PushEvent":
                    commit_count = len(event["payload"]["commits"])
                    print(f"📦 Pushed {commit_count} commit(s) to {repo_name}")
                elif type == "IssuesEvent":
                    action = event["payload"]["action"]
                    issue = event["payload"]["issue"]["title"]
                    print(f"🐞 {action.title()} issue '{issue}' in {repo_name}")
                elif type == "WatchEvent":
                    print(f"⭐ Starred {repo_name}")
                elif type == "ForkEvent":
                    forked_to = event["payload"]["forkee"]["full_name"]
                    print(f"🍴 Forked {repo_name} to {forked_to}")
                elif type == "CreateEvent":
                    ref_type = event["payload"]["ref_type"]
                    ref = event["payload"].get("ref", "")
                    print(f"🆕 Created {ref_type} {ref} in {repo_name}")
                else:
                    print(f"🔔 {type} in {repo_name}")

        elif response.status_code == 404:
            print("❌ User not found. Please check the username.")
        else:
            print(f"❌ Failed to fetch data. Status code: {response.status_code}")

    except requests.RequestException as e:
        print("❌ Network error:", str(e))
        

def main():
    if len(sys.argv)<2:
        print("Please provide the username")
        sys.exit()

    print("Output: ")
    get_user_activity(sys.argv[1])
        
   


if __name__=='__main__':
    main()
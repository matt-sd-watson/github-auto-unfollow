import sys
import requests

def get_github_data(url, headers):
    results = []
    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        results.extend(response.json())

        # GitHub paginates responses with 'Link' headers. Find the 'next' page URL if it exists.
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    return results

try:
    token = sys.argv[1] if sys.argv else None
except (KeyError, IndexError):
    token = None

headers = {"Authorization": f"token {token}"}

# Get list of users you follow
following_url = "https://api.github.com/user/following"
following = [user['login'] for user in get_github_data(following_url, headers)]

# Get list of your followers
followers_url = "https://api.github.com/user/followers"
followers = [user['login'] for user in get_github_data(followers_url, headers)]

non_followers = []
for i_follow in following:
    if i_follow not in followers:
        non_followers.append(i_follow)

for user in non_followers:
    unfollow_url = f"https://api.github.com/user/following/{user}"
    unfollow_response = requests.delete(unfollow_url, headers=headers)
    if unfollow_response.status_code == 204:
        print(f"Unfollowed {user}")
    else:
        print(f"Failed to unfollow {user}: {unfollow_response.status_code}")
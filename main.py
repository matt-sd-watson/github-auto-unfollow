import sys
import requests


def get_github_data(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


headers = {"Authorization": f"token {sys.argv[1]}"}

# Get list of users you follow
following_url = "https://api.github.com/user/following"
following = [user['login'] for user in get_github_data(following_url, headers)]

# Get list of your followers
followers_url = "https://api.github.com/user/followers"
followers = [user['login'] for user in get_github_data(followers_url, headers)]

# Find users you follow who don't follow you back
non_followers = set(following) - set(followers)

for user in non_followers:
    unfollow_url = f"https://api.github.com/user/following/{user}"
    unfollow_response = requests.delete(unfollow_url, headers=headers)
    if unfollow_response.status_code == 204:
        print(f"Unfollowed {user}")
    else:
        print(f"Failed to unfollow {user}: {unfollow_response.status_code}")
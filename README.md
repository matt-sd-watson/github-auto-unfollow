Be petty: run a Github Actions workflow that automatically unfollows anyone in my following who doesn't follow you back. 


## Usage and Installation

1. Fork this repository
2. Ensure that GitHub Actions are available to run under the repository `Settings` -> `Actions` -> `General`
3. Set up a new Personal access token [here](https://github.com/settings/tokens) by selecting `Generate new token` -> `Generate new token (classic)`
4. Under the `user` scope, add `user:follow` sub-scope
3. Under the repository settings: `Secrets and variables` -> `Actions` -> `New repository secret`, create a new secret named **GH_TOKEN**. 

The repository will curently run weekly, and can be changed in the `unfollow.yml` file under the `.github/workflows` directory using cron logic. 

The current cron schedule is set to run every Monday at 12:00. The schedule can be updated in the workflow yml:

```
name: Unfollow Non-Followers

on:
  schedule:
    # Runs at 12:00 AM every Monday
    - cron: '0 0 * * 1'
```


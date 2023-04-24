import requests
import json

print("\033[0;35mTop 5 hacker News articles:\033[0m")

hn_top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
response = requests.get(hn_top_stories_url)

if response.status_code == 200:
    hn_top_stories = json.loads(response.text)[:5]
    count = 1

    for story_id in hn_top_stories:
        story_data_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
        story_response = requests.get(story_data_url)

        if story_response.status_code == 200:
            story_data = json.loads(story_response.text)
            story_title = story_data.get('title', '')
            story_url = story_data.get('url', '')

            if story_url:
                print(f"\033[0;34m{count}. {story_title} - {story_url}\033[0m")
            else:
                print(f"\033[0;36m{count}. {story_title}\033[0m")

            count += 1
else:
    print("Error fetching top stories from Hacker News.")


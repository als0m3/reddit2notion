# Reddit 2 Notion
This Python script allows users to retrieve saved posts from their Reddit account and automatically add them to a Notion page. This allows users to keep track of their favorite posts on Reddit without having to manually search through their history.

## Roadmap
- [ ] Wait for Notion API to support Template Button creation

## Getting Started

### Prerequisites

- Python3
- pip


### Installing
Clone the repository to your local machine

```
git clone https://github.com/ALS0M3/reddit2notion.git
cd reddit2notion
```

Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configuration
The project requires a config.ini file to be filled out with the necessary information for the application to run correctly. The config.ini file should be located in the root directory of the project. Here is an example of what the config.ini file should look like:

```
[DEFAULT]
refresh_interval=5

[NOTION.secrets]
NOTION_KEY=
NOTION_DATABASE_ID=

[REDDIT.secrets]
REDDIT_USERNAME=
REDDIT_FEED_ID=
```

## Usage

### Start the programme

```
python3 main.py
```


## Tips

### Get your Reddit Feed ID

1. Go to `https://ssl.reddit.com/prefs/feeds/`
2. Click on `your saved links`
3. Copy the ID from the URL


import plotly.express as px
import requests

# GitHub username
USERNAME = "othnielObasi"

# Fetch language data from GitHub API
response = requests.get(f"https://api.github.com/users/{USERNAME}/repos")
repos = response.json()

languages = {}
for repo in repos:
    if repo['language']:
        language = repo['language']
        languages[language] = languages.get(language, 0) + 1

# Create bar chart
data = {
    'Languages': list(languages.keys()),
    'Usage': list(languages.values())
}

fig = px.bar(data, x='Usage', y='Languages', orientation='h', title='Top Languages')
fig.write_html('top_languages.html')
fig.write_image('top_languages_thumbnail.png')

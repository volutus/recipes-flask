# Recipes Flask App

For the most part, this is based on my original [self-domain Flask app.](https://github.com/volutus/self-domain-flask)

However, I knew from the start that I would be containerizing this, 
so I didn't waste time with any of the server setup logic.

- The recipes folder contains a Markdown file for each recipe that is shown on the website.
- The process_markdowns.py script generates HTML files for each Markdown file in the recipes folder.
- There are images in the static folder, but their total size is barely over 1MB. 
  - Traditionally these would be stored separately, outside of the repo. However, given their size, I just included them for ease.
  - If you add new recipes / images, **be responsible** with their file sizes.
- If you add a new recipe, just re-run the process_markdowns script and publish the updates.
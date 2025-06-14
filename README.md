# automated_book_workflow

# DAY 1
Today, I created a script using Playwright in VS Code to scrape chapter content and capture a screenshot from the specified Wikisource page. The script successfully extracts the text and saves a full-page image of the chapter. I will now push the completed work to the GitHub repository and consider Day 1's objectives achieved.

# DAY 2
Today, I implemented the AI-driven rewriting ("spinning") of the scraped chapter text using the OpenAI GPT model. The workflow includes sending the extracted content to the model via the OpenAI API and receiving a rephrased version styled in a more modern, engaging tone. The rewritten output is saved locally for further review and editing. This forms the foundation for the AI Writer agent in the automated book workflow pipeline.

✅ Tasks completed:

Integrated OpenAI API for content generation

Developed script to spin chapter text

Stored rewritten output for future human-in-the-loop feedback

# DAY 3
Today, I implemented a basic CLI-based human-in-the-loop interface to review and finalize AI-generated content. The script displays the original, AI-spun, and AI-reviewed versions of the chapter, and prompts the user to either accept the reviewed version or manually edit it before saving.

✅ Tasks Completed:

Created human_interface/editor.py to handle user review and editing

Enhanced app_day2.py to integrate human feedback into the AI workflow

Enabled a simple decision flow: accept reviewed or edit manually

Saved the finalized version to final_version.txt for version tracking

🧪 Features Implemented:

Preview first 500 characters of each version for quick comparison

CLI prompt to guide the user's decision

Manual editing supported via standard input (CTRL+D/CTRL+Z to finish)



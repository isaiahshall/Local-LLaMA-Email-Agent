# Local LLaMA3 Email Agent

This Python application leverages the Ollama LLaMA 3 model via the Ollama-python library to automatically summarize emails and generate task lists from your Gmail account. The tool integrates with the Gmail API to fetch emails, summarize their contents, and identify key action items, saving you time and enhancing productivity.

## Features

- **Email Fetching**: Connects to Gmail to retrieve emails based on specified criteria.
- **Content Summarization**: Utilizes LLaMA 3 to summarize email content.
- **Task List Generation**: Generates task lists from emails deemed important.
- **Daily Summaries**: Provides a daily summary of all important emails.

## Prerequisites

- Python 3.8 or later
- Google account with Gmail enabled
- Access to Gmail API and appropriate credentials in `credentials.json`
- Installation of required Python libraries: `ollama`, `google-auth`, `google-auth-oauthlib`, `google-api-python-client`, `bs4`

## Installation

1. Clone this repository or download the source code.
2. Install required dependencies:
   ```bash
   pip install ollama google-auth google-auth-oauthlib google-api-python-client bs4
   ```
3. Set up Gmail API credentials:
   - Follow the instructions [here](https://developers.google.com/gmail/api/quickstart/python#set_up_your_environment) to "set up your environment". This will enable the Gmail API and let your download your `credentials.json` file.

## Usage

1. Run the script:
   ```bash
   python email_summarizer.py
   ```
2. The first run will prompt you to authorize access to your Gmail through a web browser.
3. After authorization, the script will fetch new emails, summarize them, and generate a daily summary and task list, which will be saved to daily_summary.txt.

## Example Output

```
Here is the to-do list from the email summaries:

* Register for the webinar on May 21 to learn more about Transformer Models
* View billing statement now by clicking on the link provided (Westlake Financial)
* Apply by February 6th at apply.oru.edu (Oral Roberts University Online)

And here is a short written summary of highlights from all of the emails:

The past 24 hours have brought a mix of important and unimportant emails. The most notable ones include a webinar invitation on May 21 to learn about Transformer AI models, as well as an opportunity to apply for Oral Roberts University Online's degree program by February 6th. Additionally, there were several marketing or spam emails promoting various products or services, such as airport parking reservations, investment insights, and AI stocks. Overall, these emails do not require immediate attention.
```

The output files and console logs will include detailed summaries and identified tasks from your emails.

## Troubleshooting

- Ensure `token.json` is properly generated and updated if you encounter authentication errors.
- Check the console for any output errors from the Gmail API or the summarization model.

## Contributing

Feel free to fork this repository and submit pull requests. You can also open an issue if you find bugs or have feature suggestions.

## License

This project is licensed under the Apache License 2.0, which allows you to freely use, modify, and distribute this software. The license can be accessed online at [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

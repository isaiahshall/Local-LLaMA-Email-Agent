# LLEmail: Local LLaMA3 Email Agent

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
   python LLEmail.py
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

## Project Roadmap

The following is a planned list of enhancements and features that we aim to implement in the future. This roadmap is subject to change as we progress in our development and gather feedback from our users. Contributors are welcome to tackle any of these enhancements:

### Short-Term Goals
- **Adding Functionality for Additional Email Providers**
  - [ ] Integrate support for Office365 via the Microsoft Graph API.
  - [ ] Add functionality to handle emails from Yahoo using OAuth and Yahoo's Mail API.

- **User Interface Enhancements**
  - [ ] Develop a graphical user interface (GUI) to make the tool accessible for non-technical users.
  - [ ] Implement GUI elements that allow users to customize settings and view summaries interactively.

### Mid-Term Goals
- **Preset Prompt Customization for LLaMA3 8B**
  - [ ] Conduct usability testing to gather data on current prompt effectiveness.
  - [ ] Develop better preset prompt options based on testing feedback.
  - [ ] Optimize and customize prompts to improve the accuracy and relevance of generated summaries with the LLaMA3 8B model.

### Long-Term Goals
- **Extended Support and Integration**
  - [ ] Create a Telegram bot that users can interact with to receive updates and summaries directly on their mobile devices.
  - [ ] Ensure the Telegram bot supports commands for immediate interaction and scheduled summaries.

### How to Contribute
To contribute to the project, please follow the steps outlined in our `CONTRIBUTING.md` file. We encourage you to pick up tasks from the roadmap, or suggest new features or improvements by opening an issue. For major changes, please open an issue first to discuss what you would like to change.

We appreciate your interest and contributions to making this project more robust and user-friendly!

## License

This project is licensed under the Apache License 2.0, which allows you to freely use, modify, and distribute this software. The license can be accessed online at [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

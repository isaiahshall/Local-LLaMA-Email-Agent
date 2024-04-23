# Creating an email summarization / task list generating tool using Ollama with LLaMA 3, the Ollama-pyhthon library, 
# with integrations for both the Outlook and Gmail API
import os.path
from ollama import Client
import base64
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
import time

def processParts(parts):
    body_message = ""
    body_html = ""
    for part in parts:
        body = part.get("body")
        data = body.get("data")
        mimeType = part.get("mimeType")
        if mimeType == 'multipart/alternative':
            subparts = part.get('parts')
            [new_message, new_html] = processParts(subparts)
            body_message += new_message
            body_html += new_html
        elif mimeType == 'text/plain':               
            new_message = base64.urlsafe_b64decode(data)
            body_message += str(new_message, 'utf-8')
        elif mimeType == 'text/html':
            new_html = base64.urlsafe_b64decode(data)
            body_html += str(new_html, 'utf-8')
    return [body_message, body_html]

def createGmailRequest():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    emails_output = []
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", GMAIL_SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", GMAIL_SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        messages = service.users().messages().list(userId="me", q="newer_than:1d category:primary").execute()
        i = 0
        print("Collecting Gmails...")
        for message in messages["messages"]:
            i += 1
            msg = service.users().messages().get(userId="me", id=message["id"]).execute()
            subject = [header["value"] for header in msg["payload"]["headers"] if header["name"] == "Subject"]
            from_email = [header["value"] for header in msg["payload"]["headers"] if header["name"] == "From"]
            [body_message, body_html] = processParts([msg["payload"]])
            if (body_message and body_message != ""):
                content = body_message
            else:
                content = BeautifulSoup(body_html, "html.parser").text
            emails_output.append([subject, from_email, content])
            print("Email #" + str(i) + " collected")
        return emails_output
        

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


def summarizeEmails(emails_output, client):
    i = 0
    for email in emails_output:
        if not email[2] or email[2] == "":
            continue
        i+=1
        print("summarization " + str(i) + " of " + str(len(emails_output)))
        # add a timeout such that if the response takes too long, we try generating the response again

        try:
            print("LLaMA3 Input Length:" + str(len(email[2].split(" "))))
            summary = client.chat(model="llama3", stream=False, options={"num_predict": (7000 // len(emails_output)), "temperature": 0.3, "num_ctx": 8192}, messages=[
                {
                    'role': 'system',
                    'content': 'You are a powerful email-handling personal assistant that is excellent at saving me (your boss) time. Your task is to summarize the following email into a single header, with any action items listed as bullet points (action items only for IMPORTANT emails). Also, categorize the email into one of two categories IMPORTANT (/personal/work/admin) and UNIMPORTANT (marketing/spam/other). Also, if the email seems to be a template, I only care about the content that is unique to this email, not that it is a template.',
                },
                {
                    'role': 'user',
                    'content': email[2],
                }])
            email[2] = summary['message']['content']
        except:
            print("Model Timeout: Not able to summarize the following email: " + email[0])
        

def createDailySummary(emails_output, client):
    summary = client.generate(model="llama3", stream=False, options={"temperature": 0, "num_predict": 1000, "num_ctx": 8192}, system="You are a powerful email-handling personal assistant that is excellent at saving your boss time. Create a to-do list from the following email summaries which are classified as IMPORTANT. Then, provide a short written summary of highlights from all of the emails (they are from the past 24hrs)", prompt=str(emails_output))
    return summary

if __name__ == "__main__":
    client = Client(host='http://localhost:11434', timeout=240)
    try:
        client.chat(model="llama3")
    except client.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            client.pull(model="llama3")
    emails = createGmailRequest()
    print("\n All emails collected. Summarizing... \n")
    summarizeEmails(emails, client)
    print("Approx Total # of Summary Tokens" + str(len(str(emails)) // 4) + ". (A number over 7000 may result in an incomplete summary.) \n")
    print("Summarizing all emails into a daily summary... \n")
    daily_summary = createDailySummary(emails, client)["response"]
    print(daily_summary)
    with open("daily_summary.txt", "w") as file:
        file.write(daily_summary)

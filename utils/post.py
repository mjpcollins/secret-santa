import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from config.conf import settings


class Mail:

    def __init__(self, settings):
        self._settings = settings
        # If modifying these scopes, delete the file token.json.
        self._scopes = ['https://mail.google.com/']
        self._creds = self._get_credentials()
        self._service = self._get_service()
        self._user_id = 'me'

    def _get_service(self):
        return build(
            'gmail',
            'v1',
            credentials=self._creds
        )

    def send_message(self, message):
        """Send an email message.

        Args:
        message: Message to be sent.

        Returns:
        Sent Message.
        """
        message_obj = self._service.users().messages().send(
            userId=self._user_id,
            body=message
        )
        message_result = message_obj.execute()
        print(f'Message {message_result["id"]} has been sent')
        return message_result

    def _get_credentials(self):
        """
        The file token.json stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first
        time.

        :return: credentials
        """

        self._creds = None
        if os.path.exists(settings['token_path']):
            self._creds = Credentials.from_authorized_user_file(settings['token_path'], self._scopes)

        # If there are no (valid) credentials available, let the user log in.
        if not self._creds or not self._creds.valid:
            if self._creds and self._creds.expired and self._creds.refresh_token:
                self._creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(settings['creds_path'], self._scopes)
                self._creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(settings['token_path'], 'w') as token:
                token.write(self._creds.to_json())

        return self._creds



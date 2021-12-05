import base64
from email.mime.text import MIMEText


class EmailText:

    def __init__(self, settings, chain_data):
        self._settings = settings
        self._year = settings['year']
        self._subject = settings['subject']
        self._sender = settings['sender']
        self._chain_data = chain_data
        self._email_template_path = 'data/email_text.txt'

    def create_all_email_messages(self):
        return [self._create_email_message_from_chain(source)
                for source in self._chain_data['chain']]

    def _create_email_message_from_chain(self, source):
        target = self._chain_data['chain'][source]
        to = self._chain_data['emails'][source]
        message_text = self._get_email_text(
            source=source,
            target=target
        )
        return self._create_message(
            to=to,
            message_text=message_text
        )

    def _create_message(self, to, message_text):
        """
        Create a message for an email.

        Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

        Returns:
        An object containing a base64url encoded email object.
        """

        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = self._sender
        message['subject'] = self._subject
        message_bytes = message.as_string().encode('utf-8')
        message_encoded = base64.b64encode(message_bytes)
        return {'raw': message_encoded.decode('utf-8')}

    def _load_email_template(self):
        with open(self._email_template_path, 'r') as F:
            text = F.read()
        return text

    def _get_email_text(self, source, target):
        email_text = self._load_email_template()
        formatted_email = email_text.format(
            source=source,
            target=target,
            year=self._year
        )
        return formatted_email


if __name__ == '__main__':
    from utils.generate_chain import get_chain_data
    from config.conf import settings as s

    et = EmailText(
        chain_data=get_chain_data(2021),
        settings=s
    )
    m = et.create_all_email_messages()
    print()

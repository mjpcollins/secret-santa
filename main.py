from config.conf import settings
from utils.email_text import EmailText
from utils.generate_chain import get_chain_data
from utils.post import Mail


def run():
    mail_obj = Mail(settings)
    chain = get_chain_data(year=settings['year'])
    et_obj = EmailText(
        chain_data=chain,
        settings=settings
    )
    messages = et_obj.create_all_email_messages()
    for message in messages:
        mail_obj.send_message(message=message)


if __name__ == '__main__':
    run()

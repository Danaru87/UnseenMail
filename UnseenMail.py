import imaplib, os
import configparser

dirname = os.path.split(os.path.abspath(__file__))[0]

accounts = configparser.ConfigParser()
accounts.read(os.path.abspath(dirname + '/accounts.ini'))

strFormatted = ""


def check_unread(imap_account):
    if imap_account["useSSL"] == "true":
        client = imaplib.IMAP4_SSL(imap_account["host"], int(imap_account["port"]))
    else:
        client = imaplib.IMAP4(imap_account["host"], int(imap_account["port"]))
    client.login(imap_account["login"], imap_account["password"])
    client.select()
    return len(client.search(None, 'UNSEEN')[1][0].split())


for account in accounts:
    currentAccount = accounts[account]
    if account is "DEFAULT":
        continue
    if not currentAccount["icon"]:
        icon = accounts["DEFAULT"]["icon"]
    else:
        icon = currentAccount["icon"]
    unread = check_unread(currentAccount)
    strFormatted += icon + " " + str(unread) + " "
print(strFormatted)

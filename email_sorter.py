import imaplib
import email

# Configuration
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
IMAP_SERVER = "imap.gmail.com"

def clean_inbox():
    # Connect to the server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    # Search for emails with specific keyword (e.g., "Invoice")
    status, messages = mail.search(None, '(SUBJECT "Invoice")')
    
    # Loop through found emails and move them
    for num in messages[0].split():
        # Copy to "Invoices" label/folder (Folder must exist in Gmail)
        result = mail.copy(num, "Invoices")
        if result[0] == 'OK':
            # Mark as deleted in Inbox if copy was successful
            mail.store(num, '+FLAGS', '\\Deleted')
            print(f"Moved email ID {num.decode()} to Invoices folder")

    # Permanently remove deleted emails from Inbox
    mail.expunge()
    mail.logout()

if __name__ == "__main__":
    clean_inbox()

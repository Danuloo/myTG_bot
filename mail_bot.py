import imaplib
import email
from email.header import decode_header

EMAIL = "dubovich_ak24@nuwm.edu.ua"
PASSWORD = "cojx iyed nbst gvrw"

def check_mail():
    results = []  # ✅ повертаємо список знайдених листів

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, 'UNSEEN')  # тимчасово всі непрочитані
    print("Нові повідомлення:", messages[0])

    for num in messages[0].split():
        status, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])
        subject, encoding = decode_header(msg["subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors="ignore")
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        if "quiz" in body.lower() or "opens:" in body.lower():
            print("🔥 ЗНАЙДЕНО:", subject)
            results.append(f"{subject}\n{body[:300]}")  # ✅ додаємо в список

    mail.logout()
    return results  # ✅ повертаємо результат
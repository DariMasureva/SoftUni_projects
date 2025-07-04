class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while (command:= input()) != "Stop":
    sender_, receiver_, content_ = command.split()
    cur_email = Email(sender_, receiver_, content_)
    emails.append(cur_email)

send_idxs = list(map(int, input().split(", ")))

for idx in send_idxs:
    emails[idx].send()

for email in emails:
    print(email.get_info())

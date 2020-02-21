import connect
def send():
    client = connect.Connect()
    client.send_message(entity=client.get_entity("https://t.me/testAnything"),message="早")
if __name__ == '__main__':
    send()
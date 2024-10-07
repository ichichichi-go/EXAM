from webexteamssdk import WebexTeamsAPI

def create_room_and_send_message():
    access_token = input("Enter your Webex access token: ") 
    api = WebexTeamsAPI(access_token=access_token)
    
    room_name = input("Enter the room name: ")
    welcome_message = input("Enter the welcome message: ")
    
 
    room = api.rooms.create(room_name)
    print(f"Room '{room.title}' created with ID: {room.id}")
    
    message = api.messages.create(room.id, text=welcome_message)
    print(f"Message sent: {message.text}")

create_room_and_send_message()

import requests
import random
import datetime
from tkinter import *

API_KEY = "d1281936b1d866eecdf1379ed67f0f1c"
window = Tk()
window.title("ChatBot")
window.geometry("612x610")
window.config(background="#1E1E1E")
icon = PhotoImage(file="chatbotlogo2.png")
window.iconphoto(True,icon)

def get_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {now}."

def get_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    return f"Today's date is {today}."

def get_random_fact():
    facts = [
        "Honey never spoils.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries aren’t.",
        "The Eiffel Tower can grow taller in the summer due to heat expansion.",
        "A day on Venus is longer than a year on Venus."
    ]
    return random.choice(facts)
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"The weather in {city.capitalize()} is {temp}°C with {description}."
        else:
            return "I couldn't find the weather for that location."
    except:
        return "Error fetching weather data. Please check your internet connection."

def calculate(expression):
    try:
        result = eval(expression)
        return f"The answer is {result}"
    except:
        return "I couldn't calculate that. Please enter a valid math operation."

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the math book look sad? Because it had too many problems!"
    ]
    import random
    return random.choice(jokes)

def tell_story(story_type):
    stories = {
        "sad": "She typed a long message, pouring her heart out, then hesitated. 'Seen 12:03 AM.' No reply. The next morning, her phone buzzed—a text from him. 'Hey, you good?' She smiled sadly, deleted his number, and whispered, 'Too late.'",
        "horror": "It was a dark and stormy night when Sarah heard whispers coming from her closet. She thought it was the wind until she saw the closet door slowly creak open by itself. She turned on the light, but nothing was there... until she looked under her bed.",
        "romantic": "Emma and Jake met every day at the coffee shop but never spoke. One day, Jake left a note on her usual table: 'I've been waiting to say hello.' Emma smiled, wrote back, and left it for him. Their love story began with a simple exchange of notes."
    }
    return stories.get(story_type, "I don't know that kind of story yet!")

yi = 0

def clear():
    global yi
    yi = 0
    for widget in chat_bg.winfo_children():
        widget.destroy()

    chat_bg.config(bg="white")  # Ensuring background remains white


MAX_MESSAGES = 4
messages_count = 0

def send_message():
    global yi, messages_count

    if messages_count >= MAX_MESSAGES:
        clear()
        messages_count = 0

    u = user_entry.get().lower()

    user = Label(chat_bg, height=1, width=64, bg='#FFC107', text=u + '     <You', font=("Arial", 12), anchor='w')
    user.pack(anchor="w", padx=5, pady=2)

    response = "I didn't understand that. Type 'help' for assistance."

    if "hello" in u:
        response = "Hello! If you need any help, type 'help'."
    elif 'how are you' in u:
        response = "I am fine."
    elif 'hi' in u:
        response = "Hi✋, what is your name?"
    elif 'my name is' in u:
        response = "Cool name! I'm Talkie🤖. If you need any help, type 'help'."
    elif 'help' in u:
        response = "I can assist with math operations, weather info, and simple Q&A.😎"
    elif any(op in u for op in ["+", "-", "*", "/"]):
        response = calculate(u)
    elif "weather in" in u:
        city = u.replace("weather in", "").strip()
        if city:
            response = get_weather(city)
        else:
            response = "Please specify a city. Example: 'weather in New York'"
    elif 'weather' in u:
        response = "Type 'weather in [city]' in this format to find out about the current weather."
    elif 'who are you' in u:
        response = "I am Talkie, your chatbot friend! 😉"
    elif 'what can you do' in u:
        response = "I can chat, do math, fetch weather info, and answer simple questions!"
    elif 'thank you' in u or 'thanks' in u:
        response = "You're welcome! ❤"
    elif 'what is your name' in u:
        response = "I'm Talkie! What's your name?"
    elif 'tell me a joke' in u or 'joke' in u:
        response = tell_joke()
    elif 'tell me a sad story' in u:
        response = tell_story("sad")
    elif 'tell me a horror story' in u:
        response = tell_story("horror")
    elif 'tell me a romantic story' in u:
        response = tell_story("romantic")
    elif "what time is it" in u:
        response = get_time()
    elif "what is today's date" in u or "what is the date" in u:
        response = get_date()
    elif "who is the president" in u:
        response = "I'm not sure, but you can check the latest news for that."
    elif "what is python" in u:
        response = "Python is a programming language used for web development, data science, and automation."
    elif "tell me a fact" in u or "random fact" in u:
        response = get_random_fact()
    elif 'bye' in u or 'goodbye' in u:
        response = "Goodbye! Have a great day! 👋"

    bot_response = Label(chat_bg, height=4, width=64, bg='#4CAF50', text=f"Bot> {response}", font=("Arial", 12), anchor='w', wraplength=500)
    bot_response.pack(anchor="w", padx=5, pady=2)

    user_entry.delete(0, END)

    messages_count += 1

sagnik_text = Label(height=2, width=14, bg="#1E1E1E", text="Talkie", font=('Impact', 30), fg='#007ACC')
sagnik_text.pack()
chat_bg = Frame(height=420, width=592, bg="white")
chat_bg.place(x=10, y=80)
entry_bg = Frame(height=60, width=515, bg="#E0E0E0")
entry_bg.place(x=10, y=524)
send_bg = Frame(height=60, width=65, bg="white")
send_bg.place(x=538, y=524)

def on_enter(e):
    user_entry.delete(0, END)
    user_entry.config(fg="Black")

def on_leave(e):
    n = user_entry.get()
    user_entry.config(fg="Black")
    if n == '' or n == ' ':
        user_entry.insert(0, 'Message')
        user_entry.config(fg='black')

user_entry = Entry(entry_bg, width=32, bg="#FFFFFF", font=("Arial", 20), relief=FLAT, border=3)
user_entry.place(x=10, y=9)
user_entry.insert(0, 'Message')
user_entry.config(fg='black')
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)

send_button = Button(send_bg, height=1, width=3, bg="#1E1E1E", text="📤", font=('Helvetica', 20),
                     activeforeground="white", fg="white", relief=FLAT, border=0,
                     activebackground="white", command=send_message)
send_button.place(x=5, y=4)

window.mainloop()
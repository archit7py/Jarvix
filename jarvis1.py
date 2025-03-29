import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import music1


# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

api_key_news = "17166a8b9fbf493397013021241710"  # Replace with a valid API key for News API
api_key_weather = "YOUR_WEATHER_API_KEY"  # Replace with a valid API key for Weather API
api_key_gemini = "YOUR_GEMINI_API_KEY"  # Replace with a valid API key for Google Gemini AI



def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

# OPENING WEBSITES AND PLAYING MUSIC AS PER USER COMMAND
def processCommand(c):
    """Processes user voice commands."""
    c = c.lower()
    
    if "google" in c:
        webbrowser.open("https://google.com")
        speak("Here is the Google page")

    elif "facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Here is your Facebook page to log in")

    elif "youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Here is YouTube")

    elif any(day in c for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]):
        schedule = """
        At 6:30 you have to go to the gym.
        At 8:30, take breakfast.
        At 9:30, go to college.
        At 12:40, take lunch.
        Take a nap for 2 to 3 hours.
        At 4:30, wake up, and at 5, have evening snacks.
        From 5:15 to 7:15, volleyball practice.
        At 7:40, dinner.
        From 8:30 to 11:00, coding time.
        At 11:30, go to bed.
        """
        speak(schedule)

    elif "sunday" in c:
        sunday_schedule = """
        Wake up at 8:00 am.
        At 8:30, take breakfast.
        At 9:30, wash clothes.
        At 10:30, take a shower.
        At 11:00, start coding.
        At 12:30, have lunch.
        Take a nap from 1:30 for 2 to 3 hours.
        At 4:00, study for college exams.
        At 5:00, have evening snacks.
        From 5:15 to 7:15, play volleyball.
        At 7:40, dinner.
        At 8:30, code.
        At 11:30, go to bed.
        """
        speak(sunday_schedule)

    elif c.startswith("play"):
        song = c.split("play ", 1)[1]
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        speak(f"Playing {song}")

    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key_news}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                for article in articles[:5]:  # Read only top 5 headlines
                    print(article['title'])
                    speak(article['title'])
            else:
                speak("Sorry, I couldn't fetch the news.")
        except Exception as e:
            print(f"Error fetching news: {e}")
            speak("There was an error fetching the news.")

    elif "weather" in c:
        speak("Enter the city")
        city = input("Enter the city: ")
        try:
            r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key_weather}&q={city}")
            if r.status_code == 200:
                weather_data = r.json()
                temperature_c = weather_data['current']['temp_c']
                condition = weather_data['current']['condition']['text']
                weather_info = f"The temperature in {city} is {temperature_c} degrees Celsius with {condition}."
                print(weather_info)
                speak(weather_info)
            else:
                speak("Sorry, I couldn't fetch the weather information.")
        except Exception as e:
            print(f"Error fetching weather: {e}")
            speak("There was an error fetching the weather.")

    elif "nasa" in c:
        speak("Here is the astronomy picture of the day")
        webbrowser.open("https://apod.nasa.gov/apod/astropix.html")

   

if __name__ == "__main__":
    print("Jarvis is ready....")
    speak("Jarvis is ready....")
    
    while True:
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                
                if word.lower() == "jarvis":
                    speak("Yes boss")
                    with sr.Microphone() as source:
                        print("Jarvis is Activated")
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
        
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")
        
        except Exception as e:
            print(f"Error: {e}")


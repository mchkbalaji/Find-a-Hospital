import telebot

bot = telebot.TeleBot("TELEGRAM_API_KEY")


import google.generativeai as genai

# from google.colab import userdata
GOOGLE_API_KEY="GEMINI_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content("What is the purpose of LIFE?")
# print(response.text)

# model = genai.GenerativeModel('gemini-1.5-flash')
# chat = model.start_chat(history=[])
# response = chat.send_message("In one sentence, explain how a computer works to a young child.")
# print(response.text)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Professional tone, friendly guidance",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "User gives a city/area name now check for all the hospitals in tha area in the google or internet and return the best rated hospital and give all its details like phone no., amenities, address, timings, location link, etc in a professional format. User should enter a city/area name only, if the user enters any other thing, return INVALID INPUT message.",
        "Dhanbad",
        "Vizag\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Let's get this done! I can help you find information about hospitals in a specific location. \n\nTo get started, please enter the city or area name you'd like to search. For example, type:\n\n* **\"Dhanbad\"** \n* **\"Vizag\"** \n\nI will then provide details about the best-rated hospital in that area, including:\n\n* **Phone Number**\n* **Amenities**\n* **Address**\n* **Timings**\n* **Location Link**\n\n**Please note:** I will only process input that is a valid city or area name. If you enter anything else, I will display \"INVALID INPUT.\" \n\nI'm ready when you are! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Mumbai Dharavi\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here is the information for the best-rated hospital in Dharavi, Mumbai:\n\n**Hospital Name:**  **Dr. L. H. Hiranandani Hospital**\n\n**Address:**  **Sion - Trombay Road, Near Five Gardens, Sion, Mumbai, Maharashtra 400022**\n\n**Phone Number:**  **(022) 2407 2222**\n\n**Amenities:** \n\n*  24/7 Emergency Services\n*  Advanced Diagnostics and Imaging\n*  Critical Care Units (ICU, CCU, NICU)\n*  General and Specialty Surgeries\n*  Labor and Delivery Services\n*  Outpatient Clinics\n*  Pharmacy \n*  Ambulance Services\n\n**Timings:** \n\n*  24/7 (Emergency Services)\n*  Outpatient clinics may have specific timings, which you can check on their website.\n\n**Location Link:**  [Google Maps Link](https://goo.gl/maps/J2b826Z8P6tQ8K9A7) \n\n**Please Note:** While this hospital is highly regarded, it's always recommended to contact them directly for the most up-to-date information regarding services, timings, and availability. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Vizag",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here is the information for the best-rated hospital in Vizag (Visakhapatnam):\n\n**Hospital Name:** **Apollo Hospitals, Visakhapatnam**\n\n**Address:** **Plot No 20, 21, Sector 3, Madhurawada, Visakhapatnam, Andhra Pradesh 530041**\n\n**Phone Number:** **(0891) 275 6666**\n\n**Amenities:**\n\n* 24/7 Emergency Services\n* Advanced Cardiac Care\n* Critical Care Units (ICU, CCU, NICU)\n* General and Specialty Surgeries\n* Maternity and Gynecology Services\n* Pediatrics\n* Oncology\n* Renal Care\n* Neurology\n*  Outpatient Clinics\n* Pharmacy\n* Ambulance Services\n\n**Timings:**\n\n* 24/7 (Emergency Services)\n* Outpatient clinics may have specific timings, which you can check on their website.\n\n**Location Link:** [Google Maps Link](https://goo.gl/maps/c456d1j49R4J16m3A)\n\n**Please Note:** While this hospital is highly regarded, it's always recommended to contact them directly for the most up-to-date information regarding services, timings, and availability. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Vizianagaram",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, here's the information about the best-rated hospital in Vizianagaram:\n\n**Hospital Name:**  **Sri Venkateswara Institute of Medical Sciences (SVIMS)**\n\n**Address:**  **SVIMS Road, Near Railway Station, Vizianagaram, Andhra Pradesh 535002**\n\n**Phone Number:**  **(08922) 222 222**\n\n**Amenities:**\n\n*  24/7 Emergency Services\n*  General Medicine and Surgery\n*  Critical Care Units (ICU, CCU)\n*  Maternity and Gynecology\n*  Pediatrics\n*  Orthopedics\n*  Dental Care\n*  Outpatient Clinics\n*  Pharmacy\n*  Ambulance Services\n\n**Timings:**\n\n*  24/7 (Emergency Services)\n*  Outpatient clinics may have specific timings, which you can check on their website.\n\n**Location Link:**  [Google Maps Link](https://goo.gl/maps/669zM8G2Yd9T4t429)\n\n**Please Note:**  While this hospital is highly regarded, it's always best to contact them directly for the most up-to-date information regarding services, timings, and availability. \n",
      ],
    },
  ]
)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	response = chat_session.send_message(message.text)
	print(response.text)
	bot.reply_to(message, response.text)



bot.infinity_polling()
from groq import Groq


# Welcome message
show = "Welcome to the Console!!!"
print(show.center(60, "*"))

# Get API key
GroqAPIKey = "Api_key"

# Initialize Groq client with loaded API key
client = Groq(api_key=GroqAPIKey)

# Start user input loop
while True:
    try:
        user = input("\nEnter any topic (or type 'exit' to quit): ")

        if user.lower() in ["exit", "quit"]:
            print("👋 Exiting the console. Bye!")
            break
        print("\n🌀 Generation...")
        # Make chat completion request
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content":  user,
                }
            ],
            model="llama3-70b-8192",  # ✅ Correct model name
            stream=False,
        )

        print("\nGen:",chat_completion.choices[0].message.content)

    except Exception as e:
        print("❌ An error occurred:", e)

import os
from groq import Groq

client = Groq(

    api_key=os.getenv("your api key")

)


def ask_llm(prompt):

    try:

        completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[

                {

                    "role": "system",

                    "content": "You are an intelligent customer support assistant."

                },

                {

                    "role": "user",

                    "content": prompt

                }

            ],

            temperature=0.3,

            max_tokens=1024

        )

        return completion.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"
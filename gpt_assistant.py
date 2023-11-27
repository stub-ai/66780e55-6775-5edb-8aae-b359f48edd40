import openai

openai.api_key = 'your-api-key'

def gpt_assistant(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = input("Please enter your prompt: ")
    print(gpt_assistant(prompt))
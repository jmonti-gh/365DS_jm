# import openai library
import openai
print('-' * 20)
print('openai.__version__:', openai.__version__)
print('-' * 20)
print

# Set up the OpenAI API client
#openai.api_key = "sk-RU5ApKRrdoE6vChjkzfSYhqBXs2n"
openai.api_key = "sk-proj-RLfT6EVRph8ZITgA"

# this loop will let us ask questions continuously and behave like ChatGPT
while True:
    # Set up the model and prompt
    #model_engine = "text-davinci-003"
    model_engine = "gpt-3.5-turbo"
    
    prompt = input('Enter new prompt: ')

    if 'exit' in prompt or 'quit' in prompt:
        break

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # extracting useful part of response
    response = completion.choices[0].text
    
    # printing response
    print(response)

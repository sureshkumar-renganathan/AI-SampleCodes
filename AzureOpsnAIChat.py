import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI


def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        project_endpoint = "https://sureshkumarrenganathan-8262-reso.services.ai.azure.com/api/projects/sureshkumarrenganathan-8262"
        model_deployment =  "gpt-4o"

        
        # Initialize the project client
        project_client = AIProjectClient(
                credential=DefaultAzureCredential(),
                endpoint=project_endpoint
        )

         ## List all connections in the project
        connections = project_client.connections
        
        

        print("List all connections:")
        for connection in connections.list():
            print(f"{connection.name} ({connection.type})")


        # Get a chat client
        # Get a chat client
        openai_client = project_client.get_openai_client(api_version="2024-10-21")

        # Initialize prompt with system message
         # Initialize prompt with system message
        prompt = [
         {"role": "system", "content": "You are a helpful AI assistant that answers questions."}
        ]

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
            # Get a chat completion
            # Get a chat completion
            prompt.append({"role": "user", "content": input_text})
            response = openai_client.chat.completions.create(
                    model=model_deployment,
                    messages=prompt)
            completion = response.choices[0].message.content
            print(completion)
            prompt.append({"role": "assistant", "content": completion})

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()

from ollama import chat , ChatResponse
import os

# method that uses ollama chat to read the contents of the file and provide feedback
def code_checker(filename,data):
    response:ChatResponse = chat(
        model = 'codereviewer',
        messages=[
            {
                'role':'system',
                'content':'you are a friendly code reviewer that provides prompt response on /'
                          'how the code can be improved, your response should not be detailed/'
                          'short , accurate , to the point , easy to understand response is /'
                          'your characteristics'
            },
            {
                'role':'user',
                'content':f'Please review the code from the file :{filename} , data:{data} and provide optimisation feedback'
            }
        ],
        stream= False
    )
    return response

# read the contents of the file iteratively and provide the data
directory_path = 'tests/'

# List all items in the directory
items = os.listdir(directory_path)

for item in items:
    # Check if the item is a file
    if item=='__init__.py':
        continue
    if os.path.isfile(os.path.join(directory_path, item)):
        with open(os.path.join(directory_path, item), 'r') as file:
            content = file.read()
            review = code_checker(filename=item,data=content)
            print(review['message']['content'])



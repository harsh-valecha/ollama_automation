import os
from ollama import chat , ChatResponse
from datetime import datetime

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

# review files
review_comments = 'review/'

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
            # print(review['message']['content'])
            # creates a file for review comments and save the contents to it
            review_file_name = f"review_{item}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
            with open(os.path.join(review_comments,review_file_name),'w') as review_file:
                review_file.write(f"Review Comments for file :{item} , Details:\n {review['message']['content']}")
            print(f'Review file created for {item}')



from pathlib import Path
from nltk_text import top_ten

def process_file(file_path):
    # Add your logic here
    print(f"Processing: {file_path}")
    with open(file_path, 'r') as f:
        data = f.read()
        top_ten(data)
       

# Path to the directory containing your files
directory = Path('texts')

# Loop through all .txt files in the directory
for file in directory.glob('*.txt'):
    process_file(file)
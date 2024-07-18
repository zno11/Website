import os
import shutil
from bs4 import BeautifulSoup

# Define the root directory and backup directory
root_dir = os.getcwd()
backup_dir = os.path.join(root_dir, 'backup_html')

# Create the backup directory if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Get a list of all HTML files in the root directory
html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]

# Back up the HTML files
for html_file in html_files:
    shutil.copy2(os.path.join(root_dir, html_file), os.path.join(backup_dir, html_file))

# Process each HTML file to remove sections with class display-7 and beautify the HTML
for html_file in html_files:
    # Load the HTML file
    with open(os.path.join(root_dir, html_file), 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find all sections with the class display-7 and remove them
    for section in soup.find_all('section', class_='display-7'):
        section.decompose()
    
    # Replace .png with .webp in the favicon link
    for link_tag in soup.find_all('link', {'rel': 'shortcut icon'}):
        if link_tag.get('href', '').endswith('.png'):
            link_tag['href'] = link_tag['href'].replace('.png', '.webp')

    # Beautify the HTML
    beautified_html = soup.prettify()

    # Save the modified and beautified HTML back to the file
    with open(os.path.join(root_dir, html_file), 'w', encoding='utf-8') as file:
        file.write(beautified_html)

print("Sections with class 'display-7' have been removed and HTML files have been beautified. Backups have been created.")
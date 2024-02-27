import requests

def fetch_repo_tree(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def move_trailing_number(text):
  if not text:
    return text
  words = text.split()
  last_word = words[-1]
  if last_word[-1].isdigit():
    digit_start = len(last_word) - 1
    while digit_start > 0 and last_word[digit_start - 1].isdigit():
      digit_start -= 1
    number = last_word[digit_start:]
    word = last_word[:digit_start]
    words[-2:] = [word, number]
  return " ".join(words)


def format_file_name(file_name):
    return move_trailing_number(file_name.split('/')[-1].replace('_', ' ').replace('.md', '').title())


def generate_markdown_tree(tree, base_url, parent_folder=""):
    markdown = ""
    for item in tree:
        if item['type'] == 'tree':
            folder_name = format_file_name(item['path'])
            folder_url = f"{base_url}/tree/main/{item['path']}"
            markdown += f"- [{folder_name}]({folder_url})\n"
            subtree_url = item['url']
            subtree = fetch_repo_tree(subtree_url)['tree']
            markdown += generate_markdown_tree(subtree, base_url, item['path'])
        elif item['type'] == 'blob':
            file_path = f"{parent_folder}/{item['path']}" if parent_folder else item['path']
            file_name = format_file_name(file_path)
            file_url = f"{base_url}/blob/main/{file_path}"
            markdown += f"  - [{file_name}]({file_url})\n"
    return markdown


def main():
    repo_url = "https://api.github.com/repos/wasi-master/picoCTF-2022/git/trees/main?recursive=1"
    repo_tree = fetch_repo_tree(repo_url)
    if repo_tree:
        base_url = "https://github.com/wasi-master/picoCTF-2022"
        markdown_tree = generate_markdown_tree(repo_tree['tree'], base_url)
        print(markdown_tree)
    else:
        print("Failed to fetch repository tree.")

if __name__ == "__main__":
    main()

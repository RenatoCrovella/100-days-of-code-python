import requests
from bs4 import BeautifulSoup
import re
import os

def find_video_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error acessing the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links_found = []

    # Tags <video> and <source>
    for video_tag in soup.find_all('video'):
        if video_tag.get('src'):
            links_found.append(video_tag['src'])
        for source in video_tag.find_all('source'):
            if source.get('src'):
                links_found.append(source['src'])

    # Links with video extensions
    standard_video = re.compile(r'.*\.(mp4|webm|ogg)$', re.IGNORECASE)
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if standard_video.match(href):
            links_found.append(href)

    # YouTube or Vimeo iframes
    for iframe in soup.find_all('iframe'):
        src = iframe.get('src')
        if src and ("youtube.com" in src or "vimeo.com" in src):
            links_found.append(src)

    return list(set(links_found))  # Remove duplicates

def export_to_file(links, file_name='videos_found.txt'):
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            for link in links:
                f.write(link + '\n')
        print(f"\nLinks salvos em: {os.path.abspath(file_name)}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    url = input("Type the page URL: ").strip()
    videos = find_video_links(url)

    if videos:
        print("\nVideos were found:")
        for video_link in videos:
            print(video_link)

        want_save = input("\nWould you like to generate a .txt file? (y/n): ").strip().lower()
        if want_save == 'y':
            export_to_file(videos)
    else:
        print("No vídeos were found on page.")

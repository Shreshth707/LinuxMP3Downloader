import os
import sys
import subprocess

def check_requirements():
        subprocess.check_call([sys.executable, '-m', 'pip', 'install','youtube-dl'])
        
        subprocess.check_call(['sudo','apt', 'install', '-y', 'ffmpeg']) 

        os.system('clear')


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {'format': 'bestaudio/best',
    'postprocessors': [{
        
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],}



def check_input_if_url(my_url):
    base_command = 'youtube-dl -x --audio-format mp3'
    if 'youtube.com' not in my_url:
        command = base_command + f' "ytsearch1: {my_url}"'
    else:
        command = base_command + my_url

    return command




if __name__ == "__main__":
    
    check_requirements()
    
    import youtube_dl
    
    my_url = ""
    command = f'youtube-dl -x --audio-format mp3'
    print('Enter the youtube url or name of song')
    my_url = input()
    command = check_input_if_url(my_url)
    
    os.system(command)
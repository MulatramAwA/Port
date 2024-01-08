# Port!A encoder/decoder of a high-secure zip file.
# &emsp;&emsp;Install:
## &emsp;&emsp;&emsp;&emsp;1.Install Anaconda3
## &emsp;&emsp;&emsp;&emsp;2.`pip install -r requestments.txt`
# &emsp;&emsp;Use:
## &emsp;&emsp;&emsp;&emsp;`python main.py update KEY` to encode all file in folder
## &emsp;&emsp;&emsp;&emsp;`python main.py decode KEY` to decode it.
## &emsp;&emsp;&emsp;&emsp;`python main.py upload URL TOKEN` to upload into server.
## &emsp;&emsp;&emsp;&emsp;`python main.py download URL` to download from server.
# &emsp;&emsp;API:
## &emsp;&emsp;&emsp;&emsp;upload(url,token):Same as `python main.py upload url token`
## &emsp;&emsp;&emsp;&emsp;download(url):Same as `python main.py download url`
## &emsp;&emsp;&emsp;&emsp;update(key):Same as `python main.py update key`
## &emsp;&emsp;&emsp;&emsp;decode(key):Same as `python main.py decode key`
## &emsp;&emsp;&emsp;&emsp;The server that upload function send POST requests like this:
## &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{"token":"TOKEN","data":"ENCODED_DATA"}
# Thanks for you!If you want to join me,just create Pull Request!I will agree that request.
# Have fun.And don't break the LICENSE!
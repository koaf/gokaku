import requests
def r():
    
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
               'cookie': 'XSRF-TOKEN=eyJpdiI6IjNVb3RUU3dFaWRJRmFBSFFaVXFVYWc9PSIsInZhbHVlIjoiSmJCOFN6amVCaXNneGJOZDAxZmVMNW5NU2pVcmdOd3pDeFZoWTFOK0dQaS9yNXJYa2k3cjhQVXNWanJDZzhaU3RURTRPVWdGR3RXSGtYNVE5MTA2Rys4bUVEemx6YWIvZ2VEUEUzWWZzZWhWdTNJR05ET0J4ekJ0U0E1SUJJTUwiLCJtYWMiOiIwMTI0ZmUyYmM3MWFhZGYyMTcxMmRhNTBlOTI4NWJmZTVkZGIzNWI4YTFmYjFiZDNlYTg1NzBlYTFjMmNiNTQ1IiwidGFnIjoiIn0%3D; _session=eyJpdiI6IitRRjJMdFFNSExmSThwRWs2N1N4MlE9PSIsInZhbHVlIjoiNW81TThTZm52cEVPYkt4Q3MyendDTDJpVWhYWGt5aWp5K2ZZZmFwQjV3YmN3NFh3d3dyaGVQZGFjQXJ0QTdCeFFjKys4bDBXWm9pVlR6WnUzWEk3ME5uRlcrdVN6ZEU4MlJxQktUNk9rdS9sekFONzg1Zm9sdWdrZ1R1MlBPU1oiLCJtYWMiOiJjOTcwNDI5YTdiODE5YzFjYzRjNDBhNzcxY2M1YzFmN2I4OWEyMmJkYjk1NzAzZmNhMmM3MGQwM2RkYjliMzhhIiwidGFnIjoiIn0%3D'}
    comment = ('ここにコメントを記入。太糟糕了，我是大力水手! 哈哈!')
    
    ra = requests.post('https://gokakujo.jp/video/SIeUVbPl1fs/comment',
                  params={
                    '_token': 'HxAHfm3f0ISg6M1vWBQMIvvdrLCSMmG74u6WtwY0',
                    'comment': comment,
                    'btn': 'コメント'},
                headers=headers)
    print(ra)

n = 1
while (n == 1):
    r()

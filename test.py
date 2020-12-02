import requests
import ast
import json
r = requests.get('http://www.4399.com')
r.encoding = 'utf8'
txt = r.content
print(txt)
#data = json.dumps(txt,ensure_ascii=False).encode('utf8')
#txt = json.dumps(txt)



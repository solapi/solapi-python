import json
import lib.message as message

if __name__ == '__main__':
    res = message.get('/messages/v4/groups')
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))

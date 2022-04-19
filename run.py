import requests


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    massage = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = massage)
    return r.status_code


if __name__ == '__main__':
  message = '啊啊啊啊哭啊' # 要傳送的訊息內容
  token = '32NjJJG2Sl7Ulo9ASYQVYnJhfx1x1zWCwNusl6NPVMp' # 權杖值

  lineNotifyMessage(token, message)
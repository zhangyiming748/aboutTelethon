from GetSetMessages import send
import sys
def GUI():
    print("选择一个功能")
    print("1. Telegram登录道长ss网站")
    cmd = input("输入序号")
    if cmd =="q":
        return
    else:
        if cmd =="1":
            print("输入登录验证码")
            key = int(input())
            loginUserCenter(key)
def loginUserCenter(keyword):
    text=str(keyword)
    url = "https://t.me/baipiaodaozhang_bot"
    send(url,text)
    print("Done")
if __name__ == '__main__':
    GUI()
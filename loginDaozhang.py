from GetSetMessages import send
import sys
def loginUserCenter(keyword):
    text=str(keyword)
    url = "https://t.me/baipiaodaozhang_bot"
    send(url,text)
    print("Done")
if __name__ == '__main__':
    key = sys.argv[1]
    loginUserCenter(str(key))

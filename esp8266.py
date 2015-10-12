import urllib3
import time

def main():
    counter = 0
    while True:
        http = urllib3.PoolManager()
        h1 = http.request('GET', 'http://esp8266.solusipse.net')
        print h1.status
        if h1.status is 200:
            print("Page is ok!")
        counter = counter + 1
        print "You've accessed this page %d times." % counter
        print("\n going to sleep...")
        time.sleep(1)

main()

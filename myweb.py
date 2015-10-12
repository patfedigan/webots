import urllib3
import time

def main():
    counter = 0
    while True:
        http = urllib3.PoolManager()
        h1 = http.request('GET', 'http://patrickfedigan.xyz')
        h2 = http.request('GET', 'http://patrickfedigan.xyz/SpaceCreative/gallery.html')
        h3 = http.request('GET', 'http://patrickfedigan.xyz/Resume-3.pdf')
        print h1.status
        print "second:", h2.status, "third: ", h3.status
        if h1.status is 200:
            print("Page is ok!")
        counter = counter + 1
        print "You've accessed this page %d times." % counter
        print("\n going to sleep...")


main()

from TwitterAPI import TwitterAPI
import mmap
import ConfigParser

idfile = 'tweet_id.txt'
consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''
api = None

def loadCredentials(cfgfile):
    global consumer_key
    global consumer_secret
    global access_token_key
    global access_token_secret

    config = ConfigParser.ConfigParser()
    config.read(cfgfile)
    #proceed = True if 'Twitter_API_Credentials' in config.sections() else False
    #if not proceed:
    #    print "Config file either doesn't exist, or does not have section: Twitter_API_Credentials"
    #    exit()

    consumer_key = config.get('Twitter_API_Credentials', 'consumer_key')
    consumer_secret = config.get('Twitter_API_Credentials', 'consumer_secret')
    access_token_key = config.get('Twitter_API_Credentials', 'access_token_key')
    access_token_secret = config.get('Twitter_API_Credentials', 'access_token_secret')

def search():
    global api
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    r = api.request('search/tweets', {'q':'hate speech twitter bot','count':10})
    for t in r:
        tweet_id = str(t[u'id'])
        #print tweet_id
    
        try:
            f = open(idfile)
        except IOError:
            with open(idfile,'w') as f:
                print "Creating file: " + idfile
                f.write("tweet id" + '\n')
            f = open(idfile)

        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(tweet_id) != -1:
            print '= FOUND = ' + tweet_id
            f.close()
        else:
            print '= NEW TWEET = ' + tweet_id
            f.close()
            with open(idfile,'a') as f:
                print "Writing tweet_id to file..."
                f.write(tweet_id + '\n')
            
            response(t)
        print '\t'+t['user']['name']+" :: "+t['user']['screen_name']
        print '\t'+t[u'text']
            
        createURL(t)
        print
        #nr = api.request('statuses/destroy/:'+tweet_id)
        #print nr.status_code
        #print

def createURL(tweet):
    URL = 'https://twitter.com/'
    URL = URL + tweet['user']['screen_name']
    URL = URL + '/status/'
    URL = URL + str(tweet['id'])
    print '\t' + URL
    return URL

def response(tweet):
    parameters = {
        'status':'@'+tweet['user']['screen_name']+' that is not very nice'
    }
    print parameters
    rnew = api.request('statuses/update', parameters)
    print rnew.status_code

if __name__ == "__main__":
    loadCredentials('twitter_cfg.cfg')
    search()
import ConfigParser

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

filename = 'twitter_cfg.cfg'
cfgfile = open(filename,'w')
config = ConfigParser.ConfigParser()
config.add_section('Twitter_API_Credentials')
config.set('Twitter_API_Credentials','consumer_key',consumer_key)
config.set('Twitter_API_Credentials','consumer_secret',consumer_secret)
config.set('Twitter_API_Credentials','access_token_key',access_token_key)
config.set('Twitter_API_Credentials','access_token_secret',access_token_secret)
print "Writing consumer_key: " + consumer_key
print "Writing consumer_secret: " + consumer_secret
print "Writing access_token_key: " + access_token_key
print "Writing access_token_secret: " + access_token_secret
config.write(cfgfile)
cfgfile.close()
print "Finished writing cfgfile: " + filename
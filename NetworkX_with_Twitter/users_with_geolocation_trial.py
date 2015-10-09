# jedberg - 6774892 is the user.id
import tweepy

authorization_object = tweepy.OAuthHandler('90UnUQyjaq5CHoVGRYFznYPUY',
                                           '5aI3D5dGsvaIeTClvv2u7FI9jUgmvzfRsYzAjdn07M3ShTcMwe')
authorization_object.set_access_token('419380999-i2HYele4oFP5rN14b1C5CrwxlNLL6QvieHup4JtW',
                                      's4BU1gPsSTc7LcnvaQD5UyELQNLmzf9YeJrB7VAKmLGJd')
tweepy_api = tweepy.API(authorization_object)

user = tweepy_api.get_user('jedberg')

print(user)
print(user.id)

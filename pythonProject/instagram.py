from InstagramAPI import InstagramAPI

api = InstagramAPI("7043560469", "kasodiyameet@102")
api.login()


def get_ids(user_id, friends):
    gotcha = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        if friends:
            api.getUserFollowings(user_id, maxid=next_max_id)
        else:
            api.getUserFollowers(user_id, maxid=next_max_id)
        gotcha.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return gotcha


def getFollowersList():
    FollowerList = list()
    userId = api.username_id
    followers = get_ids(userId, False)
    for follower in followers:
        FollowerList.append(follower['username'])

    return FollowerList


def getFollowingList():
    FollowingList = list()
    userId = api.username_id
    followings = get_ids(userId, True)
    for following in followings:
        FollowingList.append(following['username'])

    return FollowingList



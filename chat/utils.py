import hashlib


def recognize_room_name(channel, user):
    channel_user_sorted_list = [channel, user.username]
    channel_user_sorted_list.sort()
    channel_user = "".join(channel_user_sorted_list)
    return hashlib.sha256(channel_user.encode('utf-8')).hexdigest()

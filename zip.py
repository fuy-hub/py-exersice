usernames=('Bob','Steven','Sam')
passwords=['132','546','888']
date={'yr','g','ig'}
user=zip(usernames,passwords) #只可提取一次(只可迭代一次)

print([i for i in user])
print(list(user))
user1=zip(usernames,passwords)
print({key:value for key,value in dict(user1).items() })
user2=zip(usernames,passwords,date)
print(list(user2))
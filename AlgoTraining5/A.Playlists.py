n = int(input())
# 1st person's playlist
k = int(input())
songDict = dict.fromkeys(input().split(), 1)
# other people's playlists
for i in range(n - 1):
    k = int(input())
    songList = input().split()
    for j in range(k):
        if songList[j] in songDict:
            songDict[songList[j]] += 1
# select songs liked by everyone
resPlaylist = list()
songAmount = 0
for key, value in songDict.items():
    if value == n:
        resPlaylist.append(key)
        songAmount += 1
# sort selected songs
resPlaylist.sort()
print(songAmount)
print(*resPlaylist)
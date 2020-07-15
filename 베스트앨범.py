import operator
def solution(genres, plays):
    music=dict()
    cnt=dict()
    answer=[]
    for i in range(len(genres)):
        if not genres[i] in music:
            music[genres[i]]={i:plays[i]}
            cnt[genres[i]]=plays[i]
        else:
            music[genres[i]].update({i:plays[i]})
            cnt[genres[i]]+=plays[i]
    for k in music.keys():
        music[k]=sorted(music[k].items(),key=operator.itemgetter(1),reverse=True)
    cnt=sorted(cnt.items(),key=operator.itemgetter(1),reverse=True)
    for x in cnt:
        cnt=0
        for i in music[x[0]]:
            answer.append(i[0])
            cnt+=1
            if cnt==2:break
    return answer
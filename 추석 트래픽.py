def solution(lines):
    res = 0
    time_slot=[]
    times=[]
    for log in lines:
        date,s,t=log.split(' ')
        h,m,s=s.split(':')
        back=int(h)*3600000+int(m)*60000+int(float(s)*1000)
        t=int(float(t[:-1])*1000)
        front=back-t+1
        time_slot.append([front,back])
        times.append(front)
        times.append(back)
    times.sort()
    for front in times:
        back = front +999
        cnt=0
        for f,b in time_slot:
            if front<=f<=back or front <= b <= back:
                cnt+=1
            elif f<=front and back<=b:
                cnt+=1
        res=max(cnt,res)
    return res
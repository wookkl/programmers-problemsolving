from collections import deque

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rotate = [1, -1]
n = 0


def solution(board):
    n = len(board)
    goal = [n - 1, n - 1]
    vstd = []
    q = deque()
    q.append([[0, 0], [0, 1], 0])

    while q:
        l, r, c = q.popleft()
        if r == goal:
            return c
        a = []

        for i in range(4):
            dx, dy = move[i]
            left = [sum(i) for i in zip(l, [dx, dy])]
            right = [sum(i) for i in zip(r, [dx, dy])]
            a.append([left, right, c + 1])

        for rot in rotate:
            if l[0] == r[0]:  # hor
                if 0 <= l[0] + rot <= n and 0 <= r[0] + rot < n:
                    if board[l[0] + rot][l[1]] == 0 and board[r[0] + rot][r[1]] == 0:
                        a.append([[l[0] + rot, l[1]], [l[0], l[1]], c + 1])
                        a.append([[r[0] + rot, r[1]], [r[0], r[1]], c + 1])
            else:
                if 0 <= l[1] + rot <= n and 0 <= r[1] + rot < n:
                    if board[l[0]][l[1] + rot] == 0 and board[r[0]][r[1] + rot] == 0:
                        a.append([[l[0], l[1]], [l[0], l[1] + rot], c + 1])
                        a.append([[r[0], r[1]], [r[0], r[1] + rot], c + 1])

        for ll, rr, cc in a:
            if 0 <= ll[0] < n and 0 <= ll[1] < n and 0 <= rr[0] < n and 0 <= rr[1] < n:
                if board[ll[0]][ll[1]] == 0 and board[rr[0]][rr[1]] == 0:
                    if sum(ll) > sum(rr):
                        ll, rr = rr, ll
                    if [ll, rr] not in vstd:
                        vstd.append([ll, rr])
                        q.append([ll, rr, cc])
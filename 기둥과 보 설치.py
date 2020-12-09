def is_avail(frame, frames):
    x, y, a = frame
    if a:
        if (
            [x, y - 1, 0] in frames
            or [x + 1, y - 1, 0] in frames
            or ([x - 1, y, 1] in frames and [x + 1, y, 1] in frames)
        ):
            return True
    else:
        if (
            y == 0
            or [x, y - 1, 0] in frames
            or [x, y, 1] in frames
            or [x - 1, y, 1] in frames
        ):
            return True

    return False


def solution(n, build_frame):
    frames = []
    for f in build_frame:
        frame, b = f[:3], f[3]
        if b:
            if is_avail(frame, frames):
                frames.append(frame)
        else:
            frames.remove(frame)
            isAvail = True
            for f in frames:
                if not is_avail(f, frames):
                    isAvail = False
            if isAvail is False:
                frames.append(frame)
    return sorted(frames)
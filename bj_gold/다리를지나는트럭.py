from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0 for _ in range(bridge_length)])  # 다리를 건너는 트럭
    bridge_weights = 0  # 다리를 건너는 트럭 weight의 합
    waiting = deque(truck_weights)  # 대기 트럭
    completed = 0  # 다리를 지난 트럭의 수

    while True:
        if completed == len(truck_weights):
            break

        # 다리에서 나오기
        if len(bridge) == bridge_length:
            tmp = bridge.popleft()
            bridge_weights -= tmp

            if tmp:
                completed += 1

        # 다리에 들어가기
        if len(bridge) < bridge_length:
            # 기다리는 트럭 있으면
            if waiting:
                if bridge_weights + waiting[0] <= weight:
                    tmp = waiting.popleft()
                    bridge.append(tmp)
                    bridge_weights += tmp
                else:
                    bridge.append(0)
            # 기다리는 트럭 없으면
            else:
                bridge.append(0)

        answer += 1

    return answer
'''
1번째 원소
if 1.weight > k : continue
if 1.weight <= k : 1.value

2번째 원소
if 2.weight > k : continue
if 2.weight == k : (1.value) <-> (2.value) 비교
if 2.weight < k :
    if 1.weight + 2.weight <= k: (1.value) + (2.value)
    if 1.weight + 2.weight > k: (1.value) <-> (2.value) 비교

3번째 원소
if 3.weight > k : continue
if 3.weight == k : (1,2까지의 value) <-> 3.value 비교
if 3.weight < k :
    (1, 2) (1, 3) (2, 3) (1, 2, 3) 들의 weight들 중 k보다 작거나 같은 경우를 뽑는다
    weight의 합이 k보다 작을 때, value를 비교해서 최대값을 저장한다

4번째 원소
if 4. weight > k : continue
if 4.weight == k : (1,2,3까지의 value) <-> 4.value 비교
if 4.weight < k :
    (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4) (1, 2, 3) (1, 2, 4) (2, 3, 4) (1, 2, 3, 4) 들의 weight 합 중 k보다 작거나 같은
    weight의 합이 k보다 작을 때, value를 비교해서 최대값을 저장한다
'''

import sys
thing_number, affordable_weight = map(int, sys.stdin.readline().split())
things = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(thing_number)
]


# import sys
#
# def findNewIndex(check_index, now_index):
#     global calculated_things, things, affordable_weight
#     if check_index == -1:
#         return -1
#     weight = calculated_things[check_index][0] + things[now_index][0]
#     if weight <= affordable_weight:
#         return check_index
#     else:
#         return findNewIndex(check_index - 1, now_index)
#
# thing_number, affordable_weight = map(int, sys.stdin.readline().split())
# things = [
#     list(map(int, sys.stdin.readline().split()))
#     for _ in range(thing_number)
# ]
#
# things.sort()
#
# calculated_things = []
#
# if things[0][0] <= affordable_weight: calculated_things.append(things[0])
#
# for i in range(1, thing_number):
#     # print(i)
#     new_weight = things[i][0] + calculated_things[i - 1][0]
#     new_value = 0
#     if new_weight <= affordable_weight:
#         # print("thing weight: ", things[i][0])
#         # print("new weight: ", new_weight)
#         # print("new weight <= affordable weight")
#         # print("바로 넣어버려 ~")
#         new_value = things[i][1] + calculated_things[i-1][1]
#         calculated_things.append([new_weight, new_value])
#     else:
#         # print("thing weight: ", things[i][0])
#         # print("new weight: ", new_weight)
#         # print("new weight > affordable weight")
#         # print("new index를 구하자 ~")
#         new_index = findNewIndex(i-2, i)
#         # print("new index: ", new_index)
#
#         if new_index == -1: # 등호 애매
#             # print("여태까지 넣은거 다 빼등가 새로 넣을 것만 빼등가 ")
#             # print("새로운거 하나만 넣을 때 weight: ", things[i][0])
#             # print("새로운거 하나만 넣을 때 value: ", things[i][1])
#             # print("새로운거만 뺄 때 weight: ", calculated_things[i-1][0])
#             # print("새로운거만 뺄 때 value: ", calculated_things[i - 1][1])
#             isbigger = things[i][1] > calculated_things[i-1][1]
#             new_weight = things[i][0] if isbigger else calculated_things[i-1][0]
#             new_value = things[i][1] if isbigger else calculated_things[i-1][1]
#             calculated_things.append([new_weight, new_value])
#         else:
#             # print("new index번째까지 weight: ", calculated_things[new_index][0])
#             # print("new index번째 weight + i번째 things weight: ", calculated_things[new_index][0] + things[i][0])
#             # print("new index번째 value + i번째 things value: ", calculated_things[new_index][1] + things[i][1])
#             # print("기냥 i번째 things 안받을 때 weight: ", calculated_things[i-1][0])
#             # print("기냥 i번째 things 안받을 때 value: ", calculated_things[i - 1][1])
#             isbigger = things[i][1] + calculated_things[new_index][1] > calculated_things[i-1][1]
#             new_weight = things[i][0] + calculated_things[new_index][0] if isbigger else calculated_things[i-1][0]
#             new_value = things[i][1] + calculated_things[new_index][1] if isbigger else calculated_things[i-1][1]
#             calculated_things.append([new_weight, new_value])
#     # print(calculated_things)
#     # print("==================")
#
# print(calculated_things[thing_number - 1][1])

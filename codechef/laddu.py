
# def take_input():
#     text = input().split(" ")
#     activities = int(text[0])
#     origin = text[1]
#     flag = False
#     if origin == "INDIAN":
#         flag = True
#     score = 0
#     while(activities):
#         activity = input()
#         activity_arr = activity.split(" ")
#         if activity_arr[0] == "CONTEST_WON":
#             bonus = 0
#             rank = int(activity_arr[1])
#             if rank < 20:
#                 bonus = 20 - rank
#             score += 300 + bonus
#         elif activity_arr[0] == "TOP_CONTRIBUTOR":
#             score += 300
#         elif activity_arr[0] == "BUG_FOUND":
#             score += int(activity_arr[1])
#         elif activity_arr[0] == "CONTEST_HOSTED":
#             score += 50
#         activities -= 1
#     return flag, score

t = int(input())
while(t):
    text = input().split(" ")
    activities = int(text[0])
    origin = text[1]
    flag = False
    if origin == "INDIAN":
        flag = True
    score = 0
    while activities:
        activity = input()
        activity_arr = activity.split(" ")
        if activity_arr[0] == "CONTEST_WON":
            bonus = 0
            rank = int(activity_arr[1])
            if rank < 20:
                bonus = 20 - rank
            score += 300 + bonus
        elif activity_arr[0] == "TOP_CONTRIBUTOR":
            score += 300
        elif activity_arr[0] == "BUG_FOUND":
            score += int(activity_arr[1])
        elif activity_arr[0] == "CONTEST_HOSTED":
            score += 50
        activities -= 1
    result = 0
    if(flag):
        result = int(score/200)
        print(result)
    else:
        result = int(score/400)
        print(result)
    t -= 1

        
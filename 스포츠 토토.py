import random
import time
mutd_chance = random(1, 6)
mcty_chance = random.random(1, 6)
mutd_player_choice = ["마커스 래시포드", "안토니 마시알",
                      "안토니", "크리스티안 에릭센", "브루노 페르난데스", "매과이어"]
mcty_player_choice = ["엘링 홀란", "케빈 더브라위너",
                      "훌리안 알바리즈", "필 포든", "잭 그릴리시", "후벵 디아스"]
mutd_score_list = [0, 1]
mcty_score_list = [0, 1]
mutd_score = 0
mcty_score = 0
for i in range(1, 5):
    for i in range(1, mcty_chance+1):
        mcty_score_d = random.choice(mcty_score_list)
        mcty_player = random.choice(mcty_player_choice)
        if(mcty_score_d == 1):
            mcty_score += 1
            print("맨시티의", mcty_player, "이/가 골을 넣었습니다")
    for i in range(1, mutd_chance+1):
        mutd_score_d = random.choice(mutd_score_list)
        mutd_player = random.choice(mutd_player_choice)
        if(mutd_score_d == 1):
            mutd_score += 1
            print("맨유의", mutd_player, "이/가 골을 넣었습니다")
    print("맨유", " ", mutd_score, ":", mcty_score, " ", "맨시티")
    time.sleep(2)

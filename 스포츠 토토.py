import random
import time
attack_point = 0
all_chance = random.randint(1,11)
chance = [1,2,3,4]
mutd_player_choice = ["마커스 래시포드", "안토니 마시알","안토니", "크리스티안 에릭센", "브루노 페르난데스", "해리 매과이어","카제미루","맥토미니","라파엘 바란","제이든 산초","라스무스 회이룬"]
mcty_player_choice = ["엘링 홀란", "케빈 더브라위너","훌리안 알바레즈", "필 포든", "잭 그릴리시", "후벵 디아스","베르나르두 실바","존 스톤스","카일 워커","루이스 에르난데스"]
mutd_score_list = [0, 1]
mcty_score_list = [0, 1]
mutd_score = 0
mcty_score = 0
for i in range(1,all_chance+1):
    attack_point = random.choice(chance)
    if attack_point == 1:
        mutd_score += 1
        print("맨유의",random.choice(mutd_player_choice),"선수가 골을 넣었습니다")
        print("맨유", " ", mutd_score, ":", mcty_score, " ", "맨시티")
        print("-------------------------------------------------------------------------------------------------")
        time.sleep(2) 
    elif attack_point == 2:
        mcty_score += 1
        print("맨시티의",random.choice(mcty_player_choice),"선수가 골을 넣었습니다")
        print("맨유", " ", mutd_score, ":", mcty_score, " ", "맨시티")
        print("-------------------------------------------------------------------------------------------------")
        time.sleep(2)
    elif attack_point == 3:
        print("맨유의",random.choice(mutd_player_choice),"선수가 골 찬스를 날렸습니다") 
        print("맨유", " ", mutd_score, ":", mcty_score, " ", "맨시티")
        print("-------------------------------------------------------------------------------------------------")
        time.sleep(2)  
    elif attack_point == 4:
        print("맨시티의",random.choice(mcty_player_choice),"선수가 골 찬스를 날렸습니다")
        print("맨유", " ", mutd_score, ":", mcty_score, " ", "맨시티")
        print("-------------------------------------------------------------------------------------------------")
        time.sleep(2)  
if mcty_score > mutd_score:
    print("맨시티가 승리하였습니다")        
elif mutd_score > mcty_score:
    print("맨유가 승리하였습니다")
else:
    print("무승부 입니다")             


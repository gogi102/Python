import random
import time

money = 5000


def spin():
    # 슬롯머신 회전 돌리기
    return random.choice(["🍋", "🍒", "7️⃣", "🐻", "🔔", "🥑", "🍎", "🍄", "🐷", "🐵"])


mutd_player_choice = ["마커스 래시포드", "안토니 마시알","안토니", "크리스티안 에릭센", "브루노 페르난데스", "해리 매과이어","카제미루","맥토미니","라파엘 바란","제이든 산초","라스무스 회이룬"]
mcty_player_choice = ["엘링 홀란", "케빈 더브라위너","훌리안 알바레즈", "필 포든", "잭 그릴리시", "후벵 디아스","베르나르두 실바","존 스톤스","카일 워커","루이스 에르난데스"]
madrid_player_choice = ["비니시우스 주니오르","호드리구","주드 벨링엄","토니 크로스","페데리코 발베르데","안토니오 뤼디거","추아메니","알라바","카르바할","페를랑 멘디"]
barcelona_player_choice = ["페란 토레스","주앙 펠릭스","가비","페드리","귄도안","하피냐","로베르트 레반도프스키","아라우호","크리스텐센"]




print("광주랜드에 오신 것을 환영합니다")
print("5000원 기본 금액이 지급됩니다")
print(
    "-------------------------------------------------------------------------------------------------"
)
while True:
    total_end = input("도박장을 이용하시려면 rr 나가시려면 gg를 눌러주세요(대소문자 상관 X) :")
    if total_end == "rr" or total_end == "RR":
        recharge_money = int(
            input("게임 머니 충전하시려면 1을 눌러주세요 그렇지 않으면 다른숫자를 눌러주세요"))
        if money < 0:
            money += 1
        print("현재 게임 머니가", money, "원 있습니다")
        if recharge_money == 1:
            a = int(input("충전 할 금액을 넣어주세요 :"))
            money += a
            print(a, "원 충전 되었습니다")
            print("현재 게임 머니가", money, "원 있습니다")
        print(
            "-------------------------------------------------------------------------------------------------"
        )
        print("도박장의 게임은 블랙잭과 슬롯머신이 있습니다")
        game = int(input("블랙잭은 1 슬롯머신은 2를 스포츠 토토는 3을 눌러주세요"))
        if game == 1:
            if money == 0:
                print("게임 머니가 부족합니다")
                break
            while money > 0:
                global b

                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                print("게임 블랙잭을 선택 하셨습니다")
                print("블랙잭을 실행합니다")
                print(
                    "게임 블랙잭은 딜러와의 카드 뽑기를 통해 숫자를 21에 최대한 가깝지만 21을 초과하지 않도록 해야하는 게임 입니다"
                )
                print("만약 카드 점수가 21점을 초과하게 되면 Bust되면서 게임을 패배하게 됩니다")
                print("카드는 stand로 뽑기를 멈출 수 있고 hit로 계속 카드를 뽑을 수 있습니다")
                print("만약 게임에서 승리 할 경우 베팅하였던 금액에 2배를 블랙잭으로 승리 할 경우 4배를 돌려드립니다")
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                print("현재 게임머니는", money, "원 있습니다")
                b = int(input("베팅 하십시오 000을 입력하면 올인입니다: "))
                if b > money:
                    print("게임 머니가 부족 합니다")
                    break
                if money == 0:
                    print("게임 머니가 부족합니다")
                    break
                elif b == 000 or b == money:
                    print("게임 머니 올인 입니다")
                    b = money
                    money -= money
                    money += 1
                    print("남은 게임머니는 0원 입니다")
                elif b == 0:
                    print("0원은 걸수 없습니다")
                    break
                else:
                    print("베팅 금액은", b, "원 입니다")
                    money -= b
                    money += 1
                    print("남은 게임머니는", money-1, "원 입니다")
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                #블랙잭 함수 (버그 개많음)
                def first_game():
                    # 점수 계산할 식
                    def score_sum(card_pick):
                        score = 0
                        for card in card_pick:
                            score += card
                        return score

                    # 카드 뽑기
                    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                    dealer_card = random.sample(card_list, 2)
                    my_card = random.sample(card_list, 2)
                    print("나의 카드는", my_card, "입니다")
                    show_card = random.choice(dealer_card)
                    print("딜러의 카드 중 한 장은", show_card, "입니다")
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    my_score = score_sum(my_card)
                    dealer_score = score_sum(dealer_card)
                    print("내 점수:", my_score)
                    if dealer_score < 17:
                        while True:
                            one_more_card = random.choice(card_list)
                            dealer_card.append(one_more_card)
                            dealer_score = score_sum(dealer_card)
                            if dealer_score > 16:
                                if dealer_score > 21:
                                    dealer_score = score_sum(dealer_card)
                                    if one_more_card == 11:
                                        dealer_card.remove(11)
                                        dealer_card.append(1)
                                        dealer_score = score_sum(dealer_card)
                                    if dealer_score > 16:
                                        break

                                    break
                                else:
                                    break

                    # 스코어가 21일 경우 승자 찾기
                    def winner(my_score, dealer_score):
                        global money
                        if my_score > dealer_score:
                            money = money + b * 2
                            if my_score == 21:
                                print("블랙잭입니다.")
                                money = money + b * 2
                            print("게임에서 승리하였습니다")
                            print("내 점수: ", my_score)
                            print("딜러 점수: ", dealer_score)
                            print(
                                "-------------------------------------------------------------------------------------------------"
                            )
                        elif my_score == dealer_score:
                            if my_score == 21:
                                print("블랙잭입니다.")
                            print("무승부 입니다")
                            money = money + b
                            print("딜러 점수: ", dealer_score)
                            print("내 점수: ", my_score)
                            print(
                                "-------------------------------------------------------------------------------------------------"
                            )
                        else:
                            if dealer_score == 21:
                                print("딜러의 블랙잭입니다")
                            print("딜러가 승리하였습니다")
                            print("딜러 점수: ", dealer_score)
                            print("내 점수: ", my_score)
                            print(
                                "-------------------------------------------------------------------------------------------------"
                            )

                    # 그만 아니면 이어서하기
                    def result(my_score, dealer_score):
                        global money
                        stand_hit = input("카드 뽑기를 멈추려면 stand 마저 뽑을려면 hit:")
                        while True:
                            if stand_hit == "stand":
                                if dealer_score > 21:
                                    print("딜러가 Bust 되었습니다")
                                    print("게임을 승리 하였습니다")
                                    print("딜러 점수: ", dealer_score)
                                    print("내 점수: ", my_score)
                                    print(
                                        "-------------------------------------------------------------------------------------------------"
                                    )
                                    money = money + b * 2
                                    if my_score == 21:
                                        print("블랙잭입니다")
                                        print("게임을 승리 하였습니다")
                                        money = money + b * 4
                                        print("딜러 점수: ", dealer_score)
                                        print("내 점수: ", my_score)
                                        print(
                                            "-------------------------------------------------------------------------------------------------"
                                        )
                                    break
                                else:
                                    winner(my_score, dealer_score)
                                break
                            elif stand_hit == "hit":
                                one_more_card = random.choice(card_list)
                                my_card.append(one_more_card)
                                my_score = score_sum(my_card)
                                print("내가 가진 카드는", my_card, "입니다")
                                print("내 점수는", my_score, "입니다")
                                print(
                                    "-------------------------------------------------------------------------------------------------"
                                )
                            if my_score > 21:
                                print("Bust 되셨습니다")
                                print("내 점수는", my_score, "입니다")
                                print("딜러 점수: ", dealer_score)
                                print(
                                    "-------------------------------------------------------------------------------------------------"
                                )
                                if dealer_score == 21:
                                    print("딜러가 블랙잭입니다")
                                    print("딜러가 승리하였습니다")
                                    print("내 점수는", my_score, "입니다")
                                    print("딜러 점수: ", dealer_score)
                                    print(
                                        "-------------------------------------------------------------------------------------------------"
                                    )
                                break
                            else:
                                stand_hit = input("stand 할 것인가? hit 할 것인가?")

                    result(my_score, dealer_score)
                #더 ㄱ?
                want_game = input("게임을 시작하시겠습니까? y 아니면 n(대소문자 상관 X) :")
                if want_game == "y" or want_game == "Y":
                    print("블랙잭 게임을 시작합니다")
                    first_game()
                elif want_game == "n" or want_game == "N":
                    print("블랙잭 게임을 종료합니다.")
                    break
                else:
                    break
                if money == 1:
                    print("파산하여 처음으로 이동합니다")
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    break
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                game_end3 = input("다른게임을 이용하시려면 s 이 게임을 계속하시려면 c를 쳐주세요")
                if game_end3 == "s":
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    break
                elif game_end3 == "c":
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    continue
                else:
                    print("옳지않은 요청입니다 도박장을 종료합니다")
                    break

        elif game == 2:
            if money == 0:
                print("게임 머니가 부족합니다")
                break
            while money > 0:
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                print("게임 슬롯머신을 선택 하셨습니다")
                print("슬롯머신을 실행합니다")
                print(
                    "게임 슬롯머신은  버튼을 누르면 화면에 있는 무늬가 돌아가는며 크레딧의 라인과 당첨의 조합이 일치하면 돈을 따고, 그렇지 않은 경우 돈을 잃는 게임 입니다."
                )
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                print("현재 게임머니는", money, "원 있습니다")
                c = int(input("베팅 하십시오 000을 입력하면 올인입니다: "))
                if c > money:
                    print("게임 머니가 부족 합니다")
                    break
                if money == 0:
                    print("게임 머니가 부족합니다")
                    break
                elif c == 000 or c == money:
                    print("게임 머니 올인 입니다")
                    c = money
                    money -= money
                    money += 1
                    print("남은 게임머니는 0원 입니다")
                elif c == 0:
                    print("0원은 걸수 없습니다")
                    break
                else:
                    print("베팅 금액은", c, "원 입니다")
                    money -= c
                    money += 1
                    print("남은 게임머니는", money-1, "원 입니다")
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                print("슬롯머신 게임을 시작합니다")
                result1 = spin()
                result2 = spin()
                result3 = spin()
                print(result1)
                time.sleep(0.5)
                print(" ", result2)
                time.sleep(1)
                print(" ", " ", result3)
                time.sleep(1.5)
                print(result1, result2, result3)
                if result1 == result2 and result2 == result3:
                    print("🎰잭팟입니다 5배 축하드립니다🎰")
                    money = money + c * 5
                elif result1 == result2 or result2 == result3 or result1 == result3:
                    print("🎉당첨되셨습니다 2배 축하합니다🎉")
                    money = money + c * 2

                else:
                    print("💣꽝입니다 다음 기회에....💣")
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                if money == 1:
                    print("파산하여 처음으로 이동합니다")
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    break
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                game_end1 = input("다른게임을 이용하시려면 s 이 게임을 계속하시려면 c를 쳐주세요")
                if game_end1 == "s":
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    break
                elif game_end1 == "c":
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    continue
                else:
                    print("옳지않은 요청입니다 도박장을 종료합니다")
                    break

        elif game == 3:
            if money == 0:
                print("게임 머니가 부족합니다")
                break
            while money > 0:
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                print("스포츠 토토를 시작합니다")
                print("2개의 팀중에 이길것 같은 팀을 골라서 배팅하여 2배의 배당금을 챙겨가세요")
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                #팀 선택
                choose_team = int(input("1.맨유,2.맨시티,3.레알마드리드,4.바르셀로나"))
                if choose_team == 1:
                    print("맨체스터 유나이티드를 선택하였습니다")
                elif choose_team == 2:
                    print("맨체스터 시티를 선택하였습니다")
                elif choose_team == 3:
                    print("레알마드리드를 선택하였습니다")
                elif choose_team == 4:
                    print("바르셀로나를 선택하였습니다")
                else:
                    print("옳지않은 요청입니다")
                    break                
                print("현재 게임머니는", money, "원 있습니다")
                d = int(input("베팅 하십시오 000을 입력하면 올인입니다: "))
                if d > money:
                    print("게임 머니가 부족 합니다")
                    break
                if money == 0:
                    print("게임 머니가 부족합니다")
                    break
                elif d == 000:
                    print("게임 머니 올인 입니다")
                    d = money
                    money -= money
                    money += 1
                    print("남은 게임머니는 0원 입니다")
                elif d == 0:
                    print("0원은 걸수 없습니다")
                    break
                else:
                    print("베팅 금액은", d, "원 입니다")
                    money -= d
                    money += 1
                    print("남은 게임머니는", money-1, "원 입니다")
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                #4개의 팀에 필요한 변수 and 리스트들 모음
                attack_point = 0
                all_chance = random.randint(1,11)
                chance = [1,2,3,4]
                mutd_score_list = [0, 1]
                mcty_score_list = [0, 1]
                madrid_score_list = [0,1]
                barcelona_score_list = [0,1]
                mutd_score = 0
                mcty_score = 0
                barcelona_score = 0
                madrid_score = 0
                #맨유 VS 맨시티(맨체스터 더비)
                if choose_team == 1 or choose_team == 2:
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
                        if choose_team == 2:
                          money =  money+d*2        
                    elif mutd_score > mcty_score:
                        print("맨유가 승리하였습니다")
                        if choose_team == 1:
                           money = money+d*2  
                    else:
                        print("무승부 입니다")
                        money = money+d
                else:
                    #레알 VS 바르샤(엘클라시코)
                    for i in range(1,all_chance+1):
                        attack_point = random.choice(chance)
                        if attack_point == 1:
                            madrid_score += 1
                            print("레알마드리드의",random.choice(madrid_player_choice),"선수가 골을 넣었습니다")
                            print("레알마드리드", " ", madrid_score, ":", barcelona_score, " ", "바르셀로나")
                            print("-------------------------------------------------------------------------------------------------")
                            time.sleep(2) 
                        elif attack_point == 2:
                            barcelona_score += 1
                            print("맨시티의",random.choice(barcelona_player_choice),"선수가 골을 넣었습니다")
                            print("레알마드리드", " ", madrid_score, ":", barcelona_score, " ", "바르셀로나")
                            print("-------------------------------------------------------------------------------------------------")
                            time.sleep(2)
                        elif attack_point == 3:
                            print("레알마드리드의",random.choice(madrid_player_choice),"선수가 골 찬스를 날렸습니다") 
                            print("레알마드리드", " ", madrid_score, ":", barcelona_score, " ", "바르셀로나")
                            print("-------------------------------------------------------------------------------------------------")
                            time.sleep(2)  
                        elif attack_point == 4:
                            print("바르셀로나의",random.choice(barcelona_player_choice),"선수가 골 찬스를 날렸습니다")
                            print("레알마드리드", " ", madrid_score, ":", barcelona_score, " ", "바르셀로나")
                            print("-------------------------------------------------------------------------------------------------")
                            time.sleep(2)  
                    if madrid_score > barcelona_score:
                        print("레알마드리드가 승리하였습니다")
                        if choose_team == 3:
                            money = money+d*2        
                    elif barcelona_score > madrid_score:
                        print("바르셀로나가 승리하였습니다")
                        if choose_team == 4:
                            money = money+d*2  
                    else:
                        print("무승부 입니다")
                        money = money+d           
                if money == 1:
                    print("돈이 모자라 처음으로 이동합니다")
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    break
                print(
                    "-------------------------------------------------------------------------------------------------"
                )
                game_end3 = input("다른게임을 이용하시려면 s 이 게임을 계속하시려면 c를 쳐주세요")
                if game_end3 == "s":
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    break
                elif game_end3 == "c":
                    print(
                        "-------------------------------------------------------------------------------------------------"
                    )
                    money -= 1
                    continue
                else:
                    print("옳지않은 요청입니다 도박장을 종료합니다")
    elif total_end == "gg" or total_end == "GG":
        print("도박장에서 나갑니다")
        break
    else:
        print("옳지않은 요청입니다")
        break

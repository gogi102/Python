import random
import time
money = 5000


def spin():
    return random.choice(["🍋", "🍒", "7️⃣", "🐻", "🔔"])


print("00도박장에 오신 것을 환영합니다")
while(True):
    total_end = int(input("도박장을 이용하시려면 1 나가시려면 다른숫자를 눌러주세요"))
    if total_end == 1:
        recharge_money = int(
            input("게임 머니 충전하시려면 1을 눌러주세요 그렇지 않으면 다른숫자를 눌러주세요"))
        if recharge_money == 1:
            a = int(input("충전 할 금액을 넣어주세요 :"))
            money += a
            print(a, "원 충전 되었습니다")
        print("현재 게임 머니가", money, "원 있습니다")
        print("-------------------------------------------------------------------------------------------------")
        print("도박장의 게임은 블랙잭과 슬롯머신이 있습니다")
        game = int(input("블랙잭은 1 슬롯머신은 2를 가상경마는 3을 눌러주세요"))
        if game == 1:
            if money == 0:
                print("게임 머니가 부족합니다")
                break
            while(money > 0):
                print(
                    "-------------------------------------------------------------------------------------------------")
                print("게임 블랙잭을 선택 하셨습니다")
                print("블랙잭을 실행합니다")
                print("게임 블랙잭은 딜러와의 카드 뽑기를 통해 숫자를 21에 최대한 가깝지만 21을 초과하지 않도록 해야하는 게임 입니다")
                print("카드는 스탑으로 뽑기를 멈출 수 있고 계속을 통해서 카드를 계속 뽑을 수 있습니다")
                print("만약 게임에서 승리 할 경우 베팅하였던 금액에 2배를 드립니다")
                print(
                    "-------------------------------------------------------------------------------------------------")
                print("현재 게임머니는", money, "원 있습니다")
                b = int(input("베팅 하십시오: "))
                if b > money:
                    print("게임 머니가 부족 합니다")
                    break
                if money == 0:
                    print("게임 머니가 부족합니다")
                    break
                elif b == money:
                    print("게임 머니 올인 입니다")
                    money -= b
                    money += 1
                    print("남은 게임머니는 0원 입니다")
                elif b == 0:
                    print("0원은 걸수 없습니다")
                    break
                else:
                    print("베팅 금액은", b, "원 입니다")
                    money -= b
                    print("남은 게임머니는", money, "원 입니다")
                print(
                    "-------------------------------------------------------------------------------------------------")
                # 블랙잭이 들어갈곳
                if money == 1:
                    print("돈이 모자라 처음으로 이동합니다")
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    money -= 1
                    break
                print(
                    "-------------------------------------------------------------------------------------------------")
                game_end3 = input("다른게임을 이용하시려면 s 이 게임을 계속하시려면 c를 쳐주세요")
                if game_end3 == "s":
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    break
                elif game_end3 == "c":
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    continue
                else:
                    print("옳지않은 요청입니다 도박장을 종료합니다")

        elif game == 2:
            if money == 0:
                print("게임 머니가 부족합니다")
                break
            while(money > 0):
                print(
                    "-------------------------------------------------------------------------------------------------")
                print("게임 슬롯머신을 선택 하셨습니다")
                print("슬롯머신을 실행합니다")
                print(
                    "게임 슬롯머신은  버튼을 누르면 화면에 있는 무늬가 돌아가는며 크레딧의 라인과 당첨의 조합이 일치하면 돈을 따고, 그렇지 않은 경우 돈을 잃는 게임 입니다.")
                print(
                    "-------------------------------------------------------------------------------------------------")
                print("현재 게임머니는", money, "원 있습니다")
                c = int(input("베팅 하십시오: "))
                if c > money:
                    print("게임 머니가 부족 합니다")
                    break
                if money == 0:
                    print("게임 머니가 부족합니다")
                    break
                elif c == money:
                    print("게임 머니 올인 입니다")
                    money -= c
                    money += 1
                    print("남은 게임머니는 0원 입니다")
                elif c == 0:
                    print("0원은 걸수 없습니다")
                    break
                else:
                    print("베팅 금액은", c, "원 입니다")
                    money -= c
                    print("남은 게임머니는", money, "원 입니다")
                print(
                    "-------------------------------------------------------------------------------------------------")
                print("슬롯머신 게임을 시작합니다")
                result1 = spin()
                result2 = spin()
                result3 = spin()
                print(result1)
                time.sleep(1)
                print(" ", result2)
                time.sleep(1)
                print(" ", " ", result3)
                time.sleep(1)
                print(result1, result2, result3)
                if result1 == result2 or result2 == result3 or result1 == result3:
                    print("🎉당첨되셨습니다 2배 축하합니다🎉")
                    money = money+c*2
                elif result1 == result2 and result2 == result3:
                    print("🎰잭팟입니다 5배 축하드립니다🎰")
                    money = money+c*5
                else:
                    print("💣꽝입니다 다음 기회에....💣")
                print(
                    "-------------------------------------------------------------------------------------------------")
                if money == 1:
                    print("파산하여 처음으로 이동합니다")
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    money -= 1
                    break
                print(
                    "-------------------------------------------------------------------------------------------------")
                game_end1 = input("다른게임을 이용하시려면 s 이 게임을 계속하시려면 c를 쳐주세요")
                if game_end1 == "s":
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    break
                elif game_end1 == "c":
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    continue
                else:
                    print("옳지않은 요청입니다 도박장을 종료합니다")
        elif game == 3:
            if money == 0:
                print("게임 머니가 부족합니다")
                break
            while(money > 0):
                print(
                    "-------------------------------------------------------------------------------------------------")
                print("가상경마 게임을 선택 하셨습니다")
                print("가상경마를 실행합니다")
                print("게임 가상경마는 여러 마리의 가상 말들을 동시에 출발시키고,")
                print("특정 거리를 달린 뒤 결승선을 통과하도록 경주를 시켜서 먼저 들어온 순서로 순위를 겨루는 게임 입니다")
                print(
                    "-------------------------------------------------------------------------------------------------")
                print("현재 게임머니는", money, "원 있습니다")
                d = int(input("베팅 하십시오: "))
                if d > money:
                    print("게임 머니가 부족 합니다")
                    break
                if money == 0:
                    print("게임 머니가 부족합니다")
                    break
                elif d == money:
                    print("게임 머니 올인 입니다")
                    money -= d
                    money += 1
                    print("남은 게임머니는 0원 입니다")
                elif d == 0:
                    print("0원은 걸수 없습니다")
                    break
                else:
                    print("베팅 금액은", d, "원 입니다")
                    money -= d
                    print("남은 게임머니는", money, "원 입니다")
                print(
                    "-------------------------------------------------------------------------------------------------")
                # 경마 게임이 들어갈 곳
                if money == 1:
                    print("돈이 모자라 처음으로 이동합니다")
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    money -= 1
                    break
                print(
                    "-------------------------------------------------------------------------------------------------")
                game_end3 = input("다른게임을 이용하시려면 s 이 게임을 계속하시려면 c를 쳐주세요")
                if game_end3 == "s":
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    break
                elif game_end3 == "c":
                    print(
                        "-------------------------------------------------------------------------------------------------")
                    continue
                else:
                    print("옳지않은 요청입니다 도박장을 종료합니다")
    else:
        print("도박장에서 나갑니다")
        break

import random
money = 5000
print("00도박장에 오신 것을 환영합니다")
while(True):
  total_end = input("도박장을 이용하시려면 1 나가시려면 다른숫자를 눌러주세요")
  if total_end == 1:
    recharge_money = int(input("게임 머니 충전하시려면 1을 눌러주세요 그렇지 않으면 다른숫자를 눌러주세요"))
    if recharge_money == 1:
      a = int(input("충전 할 금액을 넣어주세요 :"))
      money += a
      print(a,"원 충전 되었습니다")
    print("현재 게임 머니가",money,"원 있습니다")
    print("-------------------------------------------------------------------------------------------------")  
    print("도박장의 게임은 블랙잭과 슬롯머신이 있습니다")
    game = int(input("블랙잭은 1 슬롯머신은 2를 눌러주세요"))
    if game == 1:
      while(money > 0):
        print("-------------------------------------------------------------------------------------------------")
        print("게임 블랙잭을 선택 하셨습니다")
        print("블랙잭을 실행합니다")
        print("게임 블랙잭은 딜러와의 카드 뽑기를 통해 숫자를 21에 최대한 가깝지만 21을 초과하지 않도록 해야하는 게임 입니다")
        print("카드는 스탑으로 뽑기를 멈출 수 있고 계속을 통해서 카드를 계속 뽑을 수 있습니다")
        print("만약 게임에서 승리 할 경우 베팅하였던 금액에 2배를 드립니다")
        print("-------------------------------------------------------------------------------------------------")
        b = int(input("베팅 하십시오: "))
        print("베팅 금액은",b,"원 입니다")
        if b > money:
          print("게임 머니가 부족 합니다")
          break
        elif b == money:
          print("게임 머니 올인 입니다") 
          money -= b
          print("남은 게임머니는",money,"원 입니다")
        elif b == 0:
          print("0원은 걸수 없습니다")
          break  
        else:  
          print("베팅 금액은",b,"원 입니다") 
          money -= b
          print("남은 게임머니는",money,"원 입니다")  
        print("-------------------------------------------------------------------------------------------------")  
    elif game == 2:
      while(money > 0):
        print("-------------------------------------------------------------------------------------------------")    
        print("게임 슬롯머신을 선택 하셨습니다")
        print("슬롯머신을 실행합니다")
        print("게임 슬롯머신은  버튼을 누르면 화면에 있는 무늬가 돌아가는며 크레딧의 라인과 당첨의 조합이 일치하면 돈을 따고, 그렇지 않은 경우 돈을 잃는 게임 입니다.")
        print("-------------------------------------------------------------------------------------------------")
        c = int(input("베팅 하십시오: "))
        if c > money:
          print("게임 머니가 부족 합니다")
          break
        elif c == money:
          print("게임 머니 올인 입니다") 
          money -= c
          money += 1
          print("남은 게임머니는",money,"원 입니다")
        elif c == 0:
          print("0원은 걸수 없습니다")
          break  
        else:  
          print("베팅 금액은",c,"원 입니다")
          money -= c
          print("남은 게임머니는",money,"원 입니다")
        print("-------------------------------------------------------------------------------------------------")  
        game_end1 = input("게임을 끝내시려면 stop 계속하시려면 continue를 쳐주세요")
        if game_end1 == "stop":
          break
  else:
    print("도박장에서 나갑니다")
    break
    #게임 추가만 하면됨 아마도

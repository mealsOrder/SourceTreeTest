import random
import string
import names
import numpy as np

construction_list = ['아파트', '오피스텔', '원룸', '투룸', '빌라', '옥탑방', '반지하', '단독주택', '컨테이너']
location_list = ['하단동', '거제동', '사직동', '연산동', '부전동', '명장동', '안락동', '낙민동', '명륜동', '수안동', '온천동', '칠산동', '대연동', '문현동']
company_list = ['현대', '롯데', '대우', '럭키', '쌍용', '동원', '한화', '포스코', 'SK', '두산', '삼성']
favorite_list = ['게임', '축구', '독서', '탁구', '산책', '달리기', '싸움', '태권도', '유도', '춤', '노래', '음악', '자전거']
gn_number1 = 50
gn_number2 = 10


# test
# 테스트코드

# BMS
class BMS:
    def __init__(self):
        item_db = None

    def generate(self, gn_number1, gn_number2, item):
        item_db = ItemDB(item)
        user_db = UserDB(item)
        for i in range(gn_number1):
            item_db.add(item)

        for i in range(gn_number2):
            user_db.set_2D_list()
        # def generate_db(self, db):
        #     items = ItemDB(50000)
        #     users = UserDB(10000)

    def set_item(self):
        name = names.get_first_name(gender='female')
        price = random.randint(30, 100)
        deposit = random.randint(300, 2000)
        construction = random.choice(construction_list)
        location = random.choice(location_list)
        company = random.choice(company_list)
        img = ''.join(random.choice(string.ascii_lowercase) for i in range(4)) + ".img"
        rate = round(random.uniform(1, 10), 2)
        items = RealEstate(name, price, deposit, construction, location, company, img, rate)
        return items

    # 메뉴 출력
    def print_menu(self):
        print("1. 아이템 셋팅")
        print("2. 아이템 출력")
        print("3. 아이템 삭제")
        print("4. 아이템 검색")
        print("5. 종료")
        menu = input("메뉴 선택: ")
        return int(menu)

    # 아이템 출력
    def print_items(self, items_list):
        for items in items_list:
            items.print_info()

    # 아이템 삭제
    def delete_items(self, items_list, name):
        for i in range(len(items_list)):
            for j, items in enumerate(items_list):
                if items.name == name:
                    del items_list[j]
                    print("해당 데이터가 삭제되었습니다.")

    # 아이템 검색
    def search_items(self, items_list, name):
        for i in range(len(items_list)):
            for j, items in enumerate(items_list):
                if items.name == name:
                    return items_list[j]

    # 구동
    def run(self):
        # test_items = ["Mary", 81, 1886, "옥탑방", "온천동", "럭키", "gluc.img", 8.25]
        linked_item_list = []
        items_list = []
        search_list = []
        # load_items(items_list)
        while True:
            menu = self.print_menu()
            if menu == 1:
                number = int(input("생성할 개수: "))
                for i in range(number):
                    items = self.set_item()
                    items_list.append(items)
                self.print_items(items_list)

            elif menu == 2:
                self.print_items(items_list)
            elif menu == 3:
                name = input("Name : ")
                self.delete_items(items_list, name)
                self.print_items(items_list)
            elif menu == 4:
                search_list = []
                name = input("Name : ")
                search_list.append(self.search_items(items_list, name))
                self.print_items(search_list)
            else:
                # store_items(items_list)
                break
    # # 데이터베이스 생성
    # def generate_db(self, db):
    #     items = ItemDB(50000)
    #     users = UserDB(10000)
    #
    # # 통합검색
    # def integrated_search(self, keyword):
    #     result = []
    #     return result
    #
    # # ITEM DB 데이터베이스만 정렬
    # def integrated_sort(self, order_by='asc'):
    #     pass
    #
    # # 통합 삭제
    # def integrated_delete(self, keyword):
    #     n_delete = 0
    #     return n_delete


# 부동산 클래스
class RealEstate:
    def __init__(self, name, price, deposit, construction, location, company, img, rate):
        self.name = name  # 문자열, 건물 이름
        self.price = price  # 정수형, 월세가격(단위 : 원)
        self.deposit = deposit  # 정수형, 보증금 (단위 : 원)
        self.construction = construction  # 리스트, 건물 타입(아파트, 오피스텔, 원룸, 투룸 등등)
        self.location = location  # 문자열, 위치
        self.company = company  # 문자열, 건축한 회사
        self.img = img  # 문자열, 이미지
        self.rate = rate  # 부동소수형(float), 평점
        self.next = None

    def print_info(self):
        print(self.name, self.price, self.deposit, self.construction, self.location, self.company, self.img, self.rate)

    def storage_info(self):
        pass


# 링크드 구조 사용하기위한 노드 클래스
class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


# ItemBD :  Linked Structure 클래스
# 부모 : BMS 클래스
class ItemDB:
    def __init__(self, item):
        self.head = Node(item)

    # 추가 메소드
    def add(self, item):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(item)

    # 삭제 메소드
    # 수정 해야함 *** 중복된것 있을때 맨앞에 요소 하나만 지워짐
    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            node = self.head
            while node.next is not None:
                if node.val == item:
                    self.removeItem(item)
                    return
                node = node.next
            print("Item doesn't exist in Linked list")

    def remove_item(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                next_node = cur.next.next
                cur.next = next_node
                break

    # 출력 메소드
    def print_list(self):
        node = self.head
        print("HEAD:: ", end='')
        while node is not None:
            print(node.val, '\n->', end=' ')
            node = node.next
        if node is None:
            print('::TAIL')

    # linked list 크기값 반환 메소드
    def size(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    # 탐색 메소드
    # 수정해야함 : 중복된 아이템이 있을때 최초 발견된 아이템만 출력함
    def search(self, item):
        check = self.head
        for i in range(self.size()):
            if check.val == item:
                print(item, "The data is at the {} index.".format(i + 1))
                return None
            check = check.next
        print(item, "Data does not exist in linked list")
        return None

    # 완전탐색 메소드
    # search 메소드 수정본
    # 오류 : 중복된 값은 다 찾아내는데 다 찾아내고 나서 찾을 데이터가 없다고 출력하는 거
    def complete_search(self, data):
        check = self.head
        i = 0
        while check is not None:
            if check.val == data:
                print(data, "The data is at the {} index.".format(i + 1))
            i += 1
            check = check.next

        print(data, "Data does not exist in linked list")
        return None


# UserDB ADT
class UserDB:  # 2D List
    def __init__(self, name, age, favorite):
        self.name = name
        self.age = age
        self.favorite = favorite

    def set_2D_list(self, num):
        list_2D = [num][3]
        for i in range(num):
            for j in range(3):
                if (j % 3 == 0):
                    list_2D[i][j] = names.get_first_name(gender='female')
                if (j % 2 == 1):
                    list_2D[i][j] = random.randint(10, 100)
                if (j % 3 == 2):
                    list_2D[i][j] = random.choice(favorite_list)
        return list_2D


if __name__ == "__main__":
    bms = BMS()
    # bms.run()
    bms.generate(gn_number1, gn_number2, bms.set_item())
    linked_list = ItemDB(bms.set_item())
    linked_list.add(bms.set_item())

    linked_list.print_list()
    # real1 = RealEstate()
    # real1.print_info()

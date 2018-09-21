# coding:utf-8


class Restaurant():
    def __init__(self):
        restaurantName = ""
        cuisineType = ""
        numberServed = 0

    def describe_restaurant(self, restaurant_name, cuisine_type):
        self.restaurantName = restaurant_name
        self.cuisineType = cuisine_type
        print("餐馆名：%s,餐馆类型:%s", self.restaurantName, self.cuisineType)

    def open_restaurant(self):
        print("正在营业中，欢迎光临")

    def set_number_served(self, number_served):
        self.numberServed = number_served
        print("当时正在有%s", self.numberServed)

    def increment_number_served(self, number_added):
        self.numberServed = self.numberServed + number_added
        print("增加了%d人,当前正在就餐的人数%d", number_added, self.numberServed)


class IceCreamStand(Restaurant):
    def __init__(self):
        self.flavors = ["草莓", "香草", "奶油", "巧克力"]

    def Show(self):
        print("提供%s,%s,%s,%s口味的冰淇淋",
              self.flavors[0], self.flavors[1], self.flavors[2], self.flavors[3])

    # 重写父类的方法，只需要名字相同即可，不需要orderride关键字= =
    def describe_restaurant(self, iceCreamName):
        print("提供的冰淇淋品牌为%s", iceCreamName)


if __name__ == "__main__":
    iceStand = IceCreamStand()
    iceStand.describe_restaurant("哈根达斯")
    iceStand.Show()

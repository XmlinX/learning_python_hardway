from sys import argv
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print(f"Man that's enough for a party!")
	print(f"Get a blanket.\n")



cheese, boxes = argv
cheese_and_crackers(cheese, boxes)
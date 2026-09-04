class Hand:
        def __init__(self):
                pass

class Arms:
        def __init__(self, hand):
                self.hand = hand

class Feet:
        def __init__(self):
                pass

class Legs:
        def __init__(self, foot):
                self.foot = foot

class Head:
        def __init__(self):
                pass

class Torso:
        def __init__(self, head, arms, legs):
                self.head = head
                self.arms = arms
                self.legs = legs
                



right_hand = Hand()
left_hand = Hand()
right_arm = Arms(right_hand)
left_arm = Arms(left_hand)

right_foot = Feet()
right_leg = Legs(right_foot)
left_foot = Feet()
left_leg = Legs(left_foot)

head = Head()

arms = [right_arm, left_arm]

legs = [right_leg, left_leg]

torso = Torso(head, arms, legs)




#Test to confirm than objects point to same tag and are connected within constructor atributes
print(right_hand is right_arm.hand)
print(left_hand is left_arm.hand)
print(right_hand is left_hand)

#Test to confirm than objects point to same tag and are connected within constructor atributes
print(right_foot is right_leg.foot)
print(left_foot is left_leg.foot)
print(right_foot is left_foot)
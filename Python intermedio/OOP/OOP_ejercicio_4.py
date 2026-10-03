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
                
class Human:
        def __init__(self, head, arms, legs, torso):
                self.head = head
                self.arms = arms
                self.legs = legs
                self.torso = torso

        def get_human(self):
                for human in humans_list:
                        if self.head == human.head and self.arms == human.arms and self.legs == human.legs and self.torso == human.torso:
                                print("I am the first human")
                                return human

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

first_human = Human(head, arms, legs, torso)

humans_list = [
        first_human
]

first_human.get_human()


# Disable the following tests to avoid printing the same object multiple times, but they can be used to confirm that the objects are connected and point to the same tag.
#Test to confirm than objects point to same tag and are connected within constructor atributes
#print(right_hand is right_arm.hand)
#print(left_hand is left_arm.hand)
#print(right_hand is left_hand)

#Test to confirm than objects point to same tag and are connected within constructor atributes
#print(right_foot is right_leg.foot)
#print(left_foot is left_leg.foot)
#print(right_foot is left_foot)
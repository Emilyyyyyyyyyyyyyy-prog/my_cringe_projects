import random
import flet as ft

CARD_WIDTH = 70
CARD_HEIGHT = 100
DROP_PROXIMITY = 30
CARD_OFFSET = 20
SOLITAIRE_WIDTH = 1000
SOLITAIRE_HEIGHT = 500
SLOT_WIDTH = 70
SLOT_HEIGHT = 100


class Slot(ft.Container):
    def __init__(self, solitaire, top, left, border):
        super().__init__()
        self.pile = []
        self.width = SLOT_WIDTH
        self.height = SLOT_HEIGHT
        self.left = left
        self.top = top
        self.border = border
        self.border_radius = ft.border_radius.all(6)
        self.on_click = self.click
        self.solitaire = solitaire

    def get_top_card(self):
        if len(self.pile) > 0:
            return self.pile[-1]

    def click(self, e):
        if self == self.solitaire.stock:
            self.solitaire.restart_stock()


class Card(ft.GestureDetector):
    def __init__(self, solitaire, suite, rank):
        super().__init__()
        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 5
        self.on_pan_start = self.start_drag
        self.on_pan_update = self.drag
        self.on_pan_end = self.drop
        self.on_tap = self.click
        self.on_double_tap = self.double_click
        self.suite = suite
        self.rank = rank
        self.face_up = False
        self.left = None
        self.top = None
        self.solitaire = solitaire
        self.slot = None
        self.card_offset = CARD_OFFSET
        self.content = ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            border_radius=ft.border_radius.all(6),
            content=ft.Image(src=f"cards_pics/card_back.jpg")
        )
        self.draggable_pile = [self]

    def move_on_top(self):
        for card in self.draggable_pile:
            self.solitaire.controls.remove(card)
            self.solitaire.controls.append(card)
        self.solitaire.update()

    def bounce_back(self):
        for card in self.draggable_pile:
            card.top = card.slot.top + card.slot.pile.index(card) * CARD_OFFSET
            card.left = card.slot.left
        self.solitaire.update()

    def place(self, slot):
        for card in self.draggable_pile:
            if slot in card.solitaire.tableau:
                card.top = slot.top + len(slot.pile) * CARD_OFFSET
            else:
                card.top = slot.top
            card.left = slot.left

            if card.slot is not None:
                card.slot.pile.remove(card)
            card.slot = slot
            slot.pile.append(card)

        if self.solitaire.check_win():
            self.solitaire.winning_sequence()

        self.solitaire.update()

    def get_draggable_pile(self):
        if (
                self.slot is not None
                and self.slot != self.solitaire.stock
                and self.slot != self.solitaire.waste
        ):
            self.draggable_pile = self.slot.pile[self.slot.pile.index(self):]
        else:
            self.draggable_pile = [self]

    def start_drag(self, e: ft.DragStartEvent):
        if self.face_up:
            self.move_on_top()
            self.solitaire.update()

    def drag(self, e: ft.DragUpdateEvent):
        if self.face_up:
            for card in self.draggable_pile:
                card.top = (
                        max(0, int(self.top + e.delta_y))
                        + self.draggable_pile.index(card) * CARD_OFFSET
                )
                card.left = max(0, int(self.left + e.delta_x))
                self.solitaire.update()

    def drop(self, e: ft.DragEndEvent):
        if self.face_up:
            for slot in self.solitaire.tableau:
                if (
                        abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY
                        and abs(self.left - slot.left) < DROP_PROXIMITY
                ) and self.solitaire.check_tableau_rules(self, slot):
                    self.place(slot)
                    return

            if len(self.draggable_pile) == 1:
                for slot in self.solitaire.foundations:
                    if (
                            abs(self.top - slot.top) < DROP_PROXIMITY
                            and abs(self.left - slot.left) < DROP_PROXIMITY
                    ) and self.solitaire.check_foundations_rules(self, slot):
                        self.place(slot)
                        return

        self.bounce_back()

    def turn_face_up(self):
        self.face_up = True
        print(self.rank.name, self.suite.name)
        self.content.content = ft.Image(src=f"images/{self.rank.name}_{self.suite.name}.svg")
        self.solitaire.update()

    def click(self, e):
        if self.slot in self.solitaire.tableau:
            if not self.face_up and self == self.slot.get_top_card():
                self.turn_face_up()
        elif self.slot == self.solitaire.stock:
            self.move_on_top()
            self.place(self.solitaire.waste)
            self.turn_face_up()

    def double_click(self, e):
        self.get_draggable_pile()
        if self.face_up and len(self.draggable_pile) == 1:
            self.move_on_top()
            for slot in self.solitaire.foundations:
                if self.solitaire.check_foundations_rules(self, slot):
                    self.place(slot)
                    return


class Solitaire(ft.Stack):
    def __init__(self):
        super().__init__()
        self.controls = []
        self.slots = []
        self.width = SOLITAIRE_WIDTH
        self.height = SOLITAIRE_HEIGHT

    def did_mount(self):
        self.create_card_deck()
        self.create_slots()
        self.deal_cards()

    def create_card_deck(self):
        suites = [
            Suite("hearts", "RED"),
            Suite("diamonds", "RED"),
            Suite("clubs", "BLACK"),
            Suite("spades", "BLACK"),
        ]
        ranks = [
            Rank("Ace", 1),
            Rank("2", 2),
            Rank("3", 3),
            Rank("4", 4),
            Rank("5", 5),
            Rank("6", 6),
            Rank("7", 7),
            Rank("8", 8),
            Rank("9", 9),
            Rank("10", 10),
            Rank("Jack", 11),
            Rank("Queen", 12),
            Rank("King", 13)
        ]

        self.cards = []
        for suite in suites:
            for rank in ranks:
                self.cards.append(Card(solitaire=self, suite=suite, rank=rank))

    def create_slots(self):
        self.stock = Slot(solitaire=self, top=0, left=0, border=ft.border.all(1))
        self.waste = Slot(solitaire=self, top=0, left=100, border=None)

        self.foundations = []
        x = 300
        for i in range(4):
            self.foundations.append(Slot(solitaire=self, top=0, left=x, border=ft.border.all(1, "outline")))
            x += 100

        self.tableau = []
        x = 0
        for i in range(7):
            self.tableau.append(Slot(solitaire=self, top=150, left=x, border=None))
            x += 100

        self.controls.append(self.stock)
        self.controls.append(self.waste)
        self.controls.extend(self.foundations)
        self.controls.extend(self.tableau)
        self.update()

    def deal_cards(self):
        random.shuffle(self.cards)
        self.controls.extend(self.cards)

        first_slot = 0
        remaining_cards = self.cards

        while first_slot < len(self.tableau):
            for slot in self.tableau[first_slot:]:
                top_card = remaining_cards[0]
                top_card.place(slot)
                remaining_cards.remove(top_card)
            first_slot += 1

        for card in remaining_cards:
            card.place(self.stock)

        for slot in self.tableau:
            slot.get_top_card().turn_face_up()
            self.update()

        self.update()

    def check_foundations_rules(self, card, slot):
        top_card = slot.get_top_card()
        if top_card is not None:
            return (
                    card.suite.name == top_card.suite.name
                    and card.rank.value - top_card.rank.value == 1
            )
        else:
            return card.rank.name == "Ace"

    def check_tableau_rules(self, card, slot):
        top_card = slot.get_top_card()
        if top_card is not None:
            return (
                    card.suite.color != top_card.suite.color
                    and top_card.rank.value - card.rank.value == 1
                    and top_card.face_up
            )
        else:
            return card.rank.name == "King"

    def restart_stock(self):
        while len(self.waste.pile) > 0:
            card = self.waste.get_top_card()
            card.turn_face_down()
            card.move_on_top()
            card.place(self.stock)

    def check_win(self):
        cards_num = 0
        for slot in self.foundations:
            cards_num += len(slot.pile)
        if cards_num == 52:
            return True
        return False

    def winning_sequence(self):
        for slot in self.foundations:
            for card in slot.pile:
                card.animate_position = 1000
                card.move_on_top()
                card.top = random.randint(0, SOLITAIRE_HEIGHT)
                card.left = random.randint(0, SOLITAIRE_WIDTH)
                self.update()
        self.controls.append(ft.AlertDialog(title=ft.Text("Condratulations!! You won!!!"), open=True))


class Suite:
    def __init__(self, suite_name, suite_color):
        self.name = suite_name
        self.color = suite_color


class Rank:
    def __init__(self, card_name, card_value):
        self.name = card_name
        self.value = card_value


def main(page: ft.Page):
    solitaire = Solitaire()

    page.add(solitaire)


ft.app(target=main)

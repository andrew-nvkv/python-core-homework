class BaseAction:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return True


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')

    def __gt__(self, other):
        if other.__class__ == ScissorsAction:
            return True
        if other.__class__ == PaperAction:
            return False


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')

    def __gt__(self, other):
        if other.__class__ == RockAction:
            return True
        if other.__class__ == ScissorsAction:
            return False


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')

    def __gt__(self, other):
        if other.__class__ == PaperAction:
            return True
        if other.__class__ == RockAction:
            return False

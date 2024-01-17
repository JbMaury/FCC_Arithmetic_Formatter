
class Category:
    def __init__(self, name):
        self.name = str(name)
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category_name):
        if self.withdraw(amount, f'Transfer to {category_name.name}'):
            category_name.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def get_balance(self):
        return sum(operation["amount"] for operation in self.ledger)

    def __str__(self):
        filler_character = '*'
        max_size = 30
        number_of_fillers = (max_size - len(self.name)) // 2
        side_fillers = filler_character*number_of_fillers
        ledger_str = ''
        ledger_str += f'{side_fillers}{self.name}{side_fillers}\n'

        for operation in self.ledger:
            nb_spaces = max_size -(len(str(operation["description"])) + len(str("{:.2f}".format(operation["amount"]))))
            if nb_spaces <= 0:
                nb_spaces = 1
                operation["description"] = operation["description"][:max_size-(len(str("{:.2f}".format(operation["amount"])))+1)]
            ledger_str += f'{operation["description"]}{" " *nb_spaces}{"{:.2f}".format(operation["amount"])}\n'
        total = "{:.2f}".format(self.get_balance())
        ledger_str += f'Total: {total}'
        return ledger_str


def create_spend_chart(categories):

    # Init chart formatting
    spend_chart_str = ''
    spend_chart_title = 'Percentage spent by category\n'
    first_space = 1
    space_between_categories = 2
    separation_bar_size = len(categories)*(1 + space_between_categories) + first_space
    separation_bar_symbol = '-'
    separation_bar = separation_bar_symbol * separation_bar_size

    spend_chart_str += spend_chart_title

    # Calculate percentage by category
    withdrawal_by_category = {category.name: round(sum(operation["amount"] for operation in category.ledger if operation["amount"] < 0), 2) for category in categories}
    withdrawal_total = round(sum(withdrawal_by_category.values()), 2)
    withdrawal_percentage_by_category = {
        category_name: round((withdrawal / withdrawal_total) * 100)
        for category_name, withdrawal in withdrawal_by_category.items()}

    # Filling the chart with percentages
    for i in range(10, -1, -1):
        spend_chart_str += f'{i*10: >3}| '
        for category_name, percentage in withdrawal_percentage_by_category.items():
            if percentage >= i*10:
                spend_chart_str += 'o  '
            else:
                spend_chart_str += '   '

        spend_chart_str += '\n'
    spend_chart_str += f'{" "*4}{separation_bar}\n'

    # Adding vertically arranged name for category
    longest_word_length = max(len(category.name) for category in categories)
    for i in range(0, longest_word_length):
        # Adding starting space
        spend_chart_str += f'{" "*5}'
        for index, category in enumerate(categories):
            spend_chart_str += f'{category.name[i] if i < len(category.name) else " "}'
            spend_chart_str += f'{" "*2}'
            # Line break every end of enumeration except for the last line
            if i != longest_word_length-1 and index == len(categories)-1:
                spend_chart_str += '\n'
            # Adding space after the last letter of the last line
            elif i == longest_word_length-1 and index == len(categories)-1:
                spend_chart_str += f'{" " * ((separation_bar_size -((index*3)+2))-2)}'

    return spend_chart_str



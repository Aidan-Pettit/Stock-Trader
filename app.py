from Line import Line


def sign(number):
    if number > 0:
        return '+'
    if number < 0:
        return '-'
    if number == 0:
        return 0


def calculate_total_length(chart):
    lengths = []

    for line in chart:
        lengths.append(line.length)

    return sum(lengths)


def define_interval_values(chart):
    values = []

    for line in chart:
        i = 1

        while i <= line.length:
            values.append([line.slope, line.vertical])
            i += 1

    return values


def create_chart(data):
    chart = []
    vertical = 19.57

    for set in data:
        line = Line(set[0], set[1], vertical)
        vertical = set[0] * set[1] + vertical
        chart.append(line)

    return chart


def analyze_chart(chart):
    range = calculate_range(chart)
    extrema = find_extrema(chart)

    print('Range: ', range['highest'] - range['lowest'])
    print('Highest: ', range['highest'])
    print('Lowest: ', range['lowest'])
    print('Max Profit: ', sum(extrema))
    print('Net Change: ', chart[-1].vertical - chart[0].vertical)


def find_extrema(chart):
    extrema = []
    current_slope = 0

    for line in chart:
        if sign(line.slope) != sign(current_slope):
            if (line.slope > 0):
                extrema.append(line.vertical)
            if (line.slope < 0):
                extrema.append(line.vertical * -1)

            current_slope = line.slope

    return extrema


def calculate_range(chart):
    verticals = []

    for line in chart:
        verticals.append(line.vertical)

    lowest = min(verticals)
    highest = max(verticals)
    return {"lowest": lowest, "highest": highest}


def test_bot(data):
    chart = create_chart(data)
    values = define_interval_values(chart)
    cash = 100
    invested = 0
    current_slope = 0
    current_length = 0

    for set in values:
        current_length += 1
        print(set[0])

        # When slope of line changes
        if set[0] != current_slope:
            # Buy stock
            if set[0] > 0:
                invested = cash
                cash = 0
                current_length = 0
                current_slope = set[0]
            # Sell stock
            if set[0] < 0:
                cash = invested + (invested * current_slope * current_length)
                print(cash)
                print(invested)
                invested = 0
                current_length = 0
                current_slope = set[0]

    if cash == 0:
        cash = invested

    return cash


data = [[0.23, 7], [0.5, 1], [0, 3], [-0.33, 10],
        [0.8, 3], [0.07, 60], [-0.13, 13]]


# Function calls
profit = test_bot(data)
print(profit)

# print(define_interval_values(create_chart(data)))
# chart = create_chart(data)
# analyze_chart(chart)

# Timothy Metzger
# Input: Maximum Heart Rate
# Output: Graph of hear rate training zones

import matplotlib.pyplot as plt


def verifyInput(value, q):
    """Verifies that users input is a number
    Keyword args:
        value -- user's input value
        q -- question to user
    """
    try:
        value = int(value)
        return value
    except ValueError:
        return verifyInput(input(q), q)


def main():
    max_hr = verifyInput(input(q := "Enter your maximum heart rate: "), q)
    zone_dist = [[63, 73], [73, 80], [80, 87], [87, 93], [93, 100]]
    lower_zones = []
    upper_zones = []

    for zone in zone_dist:
        lower_bound = zone[0] * max_hr / 100
        upper_bound = zone[1] * max_hr / 100
        lower_zones.append(lower_bound)
        upper_zones.append(upper_bound)

    plt.figure()
    plt.style.use('seaborn-dark')
    plt.ylim([lower_zones[0], upper_zones[4]])
    labels = [f'Zone {i + 1} - ({lower_zones[i]}-{upper_zones[i]})' for i in range(5)]

    upper_zones = [upper_zones[i] - lower_zones[i] for i in range(len(lower_zones))]
    colors = ['blue', 'green', 'yellow', 'orange', 'red']

    for count, color in enumerate(colors):
        plt.bar(x=count + 1, height=upper_zones[count], color=color, bottom=lower_zones[count], width=1,
                label=labels[count], edgecolor='black')

    plt.xlabel('Zones')
    plt.xticks([])
    plt.ylabel('Heart Rate')
    plt.yticks(ticks=range(int(lower_zones[0]), max_hr + 1, 5))
    plt.title('Heart Rate Training Zones by Maximum Heart Rate')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

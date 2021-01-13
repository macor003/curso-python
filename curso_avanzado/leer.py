def run():
    counter = 0
    with open('aleph.txt') as file:
        for line in file:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra ' + str(counter) + ' veces en el texto')


if __name__ == '__main__':
    run()

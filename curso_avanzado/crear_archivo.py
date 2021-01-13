def run():
    with open('numeros.txt', 'w') as file:
        for i in range(10):
            file.write(str(i) + '\n')


if __name__ == '__main__':
    run()

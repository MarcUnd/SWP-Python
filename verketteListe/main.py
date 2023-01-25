import marcList as ml

def main():
    test = ml.marcList('start')
    test.addItem('end')
    test.addItem('hi')
    test.addItem('yo')
    print(test.startElem)
    print(test)
    if not test.isInList('yoo'):
        test.addItem('yoo')
    print(test)
    print(test.getByIndex(2))
    #print(test.getIndex('end'))
    num = ml.marcList(10)
    num.addItem(2)
    num.addItem(3)
    test.addItem(num)
    print(test)
    #print(test.getIndex(num))


if __name__ == '__main__':
    main()
import marcList as ml

def main():
    test = ml.marcList(1, 2, 3, 5, 8, 5)
    test.append('end')
    test.append('hi')
    test.append('yo')
    
    print(test)
    test.insert('hallo',5)
    print(test)
    
    
    
    
    


if __name__ == '__main__':
    main()
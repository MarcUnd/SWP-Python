import marcList as ml

def main():
    test = ml.marcList(1, 2, 3, 5, 8, 5)
    test.append('end')
    test.append('hi')
    test.append('yo')
    
    yo = test.copy()
    
    print(yo)
    
    
    
if __name__ == '__main__':
    main()
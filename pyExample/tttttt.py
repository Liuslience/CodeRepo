
# If you need to import additional packages or classes, please import here.

def func():
    try:
        while True:
            n = int(input())
            card = input().split(' ')
            stack = []
            for i in range(len(card)):
                if len(stack) <2:
                    stack.append(card[i])
                else:
                    if stack[-1] == card[i] and stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                    else:
                        stack.append(card[i])
            if len(stack) == 0:
                print(0)
            print(''.join(stack))
            #print(stack)
            #print('\n')
    except:
        pass
    
    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().

if __name__ == "__main__":
    func()

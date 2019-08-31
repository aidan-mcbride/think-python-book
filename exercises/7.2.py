# exercises/7.2.py

def eval_loop():
    eval_return = None
    while True:
        print("Enter a statement to be evaluated:", end=" ")
        user_input = str(input())
        if user_input == 'done':
            return eval_return
        eval_return = eval(user_input)
        print(eval_return)

print(eval_loop())

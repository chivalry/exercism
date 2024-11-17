def square_root(number):
    for root in range(number + 1):
        if root * root == number:
            return root

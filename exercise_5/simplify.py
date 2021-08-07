def is_good_index(i):
    if i > 0:
        return True
    return False


def get_numbers(n):
    result = []
    for i in range(1, n + 1):
        if is_good_index(i):
            result.append(1)
    return result


def do_some_calculations(n):
    val = 0
    for i in range(n):
        val += i
    numbers = get_numbers(n)
    val = sum(numbers)
    return val


"""
ჩემი ვერსია:

როგორც ვხვდები, ფუნქციების ეს კასკადი იმას ემსახურება, რომ მომხმარებლისგან აიღოს რიცხვი და შექმნას 
ამ რიცხვის შესაბამისი რაოდენობის ერთიანების მასივი/ლისტი. (ამას შვება get_numbers ფუნქცია)
ხოლო do_some_calculation აკეთებს იმას, რომ ამ ეთიიანაბს აჯამებს იმდენჯერ, რა რიცხვიც შეიყვანა მომხმარებელმა
ანუ, თუ მომხმარებელი წერს 1-ს მაშინ მასივი [1] და ჯამიი 1, თუ 3, მასივი - [1,1,1] ჯამი - 3.
თუ მომხმარებელი შეიყვანს 0-ს, მასივიი ცარიელი იქნება, ხოლო ჯამმი 0

"""


def final(number):
    return number


def main():
    n = int(input('Enter some number: '))
    print(final(n))



if __name__ == '__main__':
    main()

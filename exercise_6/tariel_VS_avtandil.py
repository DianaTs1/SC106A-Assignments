def main():
    avtandil = 0
    tariel = 0

    with open("poem.txt", encoding='utf-8') as poem:
        for line in poem:
            if "ავთანდილ" in line:
                avtandil += 1
            if "ტარიელ" in line:  # აქ if-ის მაგივრად elif-ს რომ ვწერ, 134-ს მიწერდა იმიტომ, რომ იმ ხაზებს, სადაც ტარიელი და ავთანდილი ერთად წერია, აიგნორებდა
                tariel += 1
        print(f'"ვეფხისტყაოსანში" ავთანდილი {avtandil}-ჯერ არის ნახსენები, ტარიელი კი - {tariel}-ჯერ.')


if __name__ == '__main__':
    main()

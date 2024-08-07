class Solution:
    def __init__(self):
        self.zero_to_twenty = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }

        self.twenty_to_hundred = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
    def numberToWords(self, num: int) -> str:
        str_num = str(num)
        assert len(str_num) <= 10   # Since 0 <= num <= 2^31 - 1

        hundreds = str_num[-3:]
        thousands = str_num[-6:-3]
        millions = str_num[-9:-6]
        billions = str_num[-12:-9]
        assert len(billions) <= 1

        words_to_join = [
            self.billionsHelper(billions),
            self.millionsHelper(millions),
            self.thousandsHelper(thousands),
            self.hundredsHelper(hundreds)
        ]
        
        return " ".join(filter(lambda word: word != "", words_to_join)).strip()
    
    def hundredsHelper(self, str_num):
        assert len(str_num) <= 3
        
        # self.zero_to_twenty ==> 0-19
        # self.twenty_to_hundred ==> 2-9, (represents 20-90 with skip=10)

        if len(str_num) == 0:
            return ""
        
        if len(str_num) == 1 or (len(str_num) == 2 and int(str_num[0]) <= 1):
            assert int(str_num) in self.zero_to_twenty
            return self.zero_to_twenty[int(str_num)]

        if len(str_num) == 2:
            first_digit, second_digit = str_num[0], str_num[1]
            assert int(first_digit) >= 2

            tens_word = self.twenty_to_hundred[int(first_digit)]
            if int(second_digit) == 0:
                return tens_word
            singles_word = self.zero_to_twenty[int(second_digit)]
            return f"{tens_word} {singles_word}"
        
        assert len(str_num) == 3
        first, second, third = str_num # digits
        hundreds = f"{self.zero_to_twenty[int(first)]} Hundred"
        if hundreds == "Zero Hundred":
            hundreds = ""
        rest_of_word = self.hundredsHelper(str_num[1:])
        if rest_of_word == "Zero":
            return hundreds
        return f"{hundreds} {rest_of_word}".strip()


    def thousandsHelper(self, str_num):
        assert len(str_num) <= 3
        word = self.hundredsHelper(str_num)
        return f"{word} Thousand" if len(word) > 0 else ""
    
    def millionsHelper(self, str_num):
        assert len(str_num) <= 3
        word = self.hundredsHelper(str_num)
        return f"{word} Million" if len(word) > 0 else ""
    
    def billionsHelper(self, str_num):
        assert len(str_num) <= 3
        word = self.hundredsHelper(str_num)
        return f"{word} Billion" if len(word) > 0 else ""
public class Solution {
    public int[] PlusOne(int[] digits) {
        return PlusOneRec(digits, digits.Length - 1);
    }
    private int[] PlusOneRec(int[] digits, int index)
    {
        if (digits[index] < 9)
        {
            digits[index]++;
            return digits;
        }

        // digits[index] == 9
        digits[index] = 0;
        if (index == 0)
        {
            int[] new_digits = new int[digits.Length + 1];
            new_digits[0] = 1;
            for (int i = 0; i < digits.Length; i++)
                new_digits[i + 1] = digits[i];
            
            return new_digits;
        }

        return PlusOneRec(digits, index - 1);
    }
}
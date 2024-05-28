public class Solution {
    public void Rotate(int[][] matrix) {
        // Idea: Transpose, then reverse rows

        // First, transpose matrix
        int n = matrix.Length;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
            {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        
        // Now, reverse rows
        for (int i = 0; i < n; i++)
        {
            int[] row = matrix[i];
            int left = 0, right = n - 1;
            while (left < right)
            {
                // Swap logic
                int tmp = row[left];
                row[left] = row[right];
                row[right] = tmp;

                // Loop invariant
                left++; right--;
            }
        }

        return;
    }
}
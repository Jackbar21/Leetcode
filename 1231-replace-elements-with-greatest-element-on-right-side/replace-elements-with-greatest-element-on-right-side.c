/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize) {
    *returnSize = arrSize;
    int* res = malloc(arrSize * sizeof(int));

    if (arrSize <= 0)
        return res;
    
    if (arrSize == 1)
    {
        res[0] = -1;
        return res;
    }

    int biggest = arr[arrSize - 1];
    res[arrSize - 1] = -1;

    int index = arrSize - 2;
    while (index >= 0)
    {
        int tmp = arr[index];
        res[index] = biggest;
        if (tmp > biggest)
            biggest = tmp;

        // Loop Invariant
        index--;
    }

    return res;
}
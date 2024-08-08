import random
import timeit

# MEDIAN OF MEDIANS FUNCTION
def MMSelection(arr, k, low, high):
    while True:
        n = high - low + 1
        if n < 5:
            arr[low:high + 1] = sorted(arr[low:high + 1])
            return arr[low + k - 1]

        num_medians = (n + 4) // 5
        medians = []

        for i in range(num_medians):
            median_low = low + i * 5
            median_high = min(low + i * 5 + 4, high)
            median = arr[median_low:median_high + 1]
            median.sort()
            medians.append(median[len(median) // 2])

        pivot = MMSelection(medians, len(medians) // 2 + 1, 0, len(medians) - 1)

        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1

        if k == pivot_index - low + 1:
            return arr[pivot_index]
        elif k < pivot_index - low + 1:
            high = pivot_index - 1
        else:
            k -= pivot_index - low + 1
            low = pivot_index + 1

# USING RANDOMIZED SEARCH
def RSelection(arr, low, high, k):
    array_size = high - low + 1
    if k > 0 and k <= array_size:
        randspot = random.randint(low, high)
        arr[low], arr[randspot] = arr[randspot], arr[low]
        pivotitem = arr[low]
        j = low

        for i in range(low + 1, high + 1):
            if arr[i] < pivotitem:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        randspot = j
        arr[low], arr[randspot] = arr[randspot], arr[low]

        if k == randspot - low + 1:
            return arr[randspot]
        elif k < randspot - low + 1:
            return RSelection(arr, low, randspot - 1, k)
        else:
            return RSelection(arr, randspot + 1, high, k - (randspot - low + 1))
    else:
        return None

# Worst case example
print("------------------------------------")
print("WORST CASE EXAMPLE")
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k1 = 7

start_time1 = timeit.default_timer()
mm_result1 = MMSelection(A, k1, 0, len(A) - 1)
end_time1 = timeit.default_timer()
print(f"Time taken by MMSelection: {(end_time1 - start_time1) * 10**9} nanoseconds")

start_time2 = timeit.default_timer()
random_result1 = RSelection(A, 0, len(A) - 1, k1)
end_time2 = timeit.default_timer()
print(f"Time taken by RSelection: {(end_time2 - start_time2) * 10**9} nanoseconds")

print("\nUSING MEDIAN OF MEDIANS SEARCH")
print(f"The {k1}-th smallest element is: {mm_result1}")
print("\nUSING RANDOMIZED SEARCH")
print(f"The {k1}-th smallest element is:", random_result1)


# Random data set example
print("------------------------------------")
print("RANDOM DATA SET EXAMPLE")
B = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k2 = 2

start_time1 = timeit.default_timer()
mm_result2 = MMSelection(B, k2, 0, len(B) - 1)
end_time1 = timeit.default_timer()
print(f"Time taken by MMSelection: {(end_time1 - start_time1) * 10**9} nanoseconds")

start_time2 = timeit.default_timer()
random_result2 = RSelection(B, 0, len(B) - 1, k2)
end_time2 = timeit.default_timer()
print(f"Time taken by RSelection: {(end_time2 - start_time2) * 10**9} nanoseconds")

print("\nUSING MEDIAN OF MEDIANS SEARCH")
print(f"The {k2}-th smallest element is: {mm_result2}")
print("\nUSING RANDOMIZED SEARCH")
print(f"The {k2}-th smallest element is:", random_result2)


# Compare performance for increasing array sizes
for n in range(5, 50, 5):  # Odd multiples of 5
    A = [random.randint(1, 100) for _ in range(n)]
    k = n // 2 + 1  # Choose k for worst-case scenario

    print("------------------------------------")
    print(f"Array Size: {n}, k: {k}")

    # Measure performance of MMSelection
    MM_start = timeit.default_timer()
    MM_result = MMSelection(A, k, 0, len(A) - 1)
    MM_end = timeit.default_timer()
    print(f"MMSelection Result: {MM_result}, Time taken: {(MM_end - MM_start) * 10**9} nanoseconds")

    # Measure performance of RSelection
    R_start = timeit.default_timer()
    R_result = RSelection(A, 0, len(A) - 1, k)
    R_end = timeit.default_timer()
    print(f"RSelection Result: {R_result}, Time taken: {(R_end - R_start) * 10**9} nanoseconds")

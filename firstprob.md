
# Closest Point Problem

## Problem Description

You are given a set of points on a number line. The distance between any two points `i` and `j` is defined as the absolute difference `|i - j|`.

A point `i` from the set is considered the closest to point `j` from the set if there is no other point `k` such that the distance from `j` to `k` is strictly less than the distance from `j` to `i`. In other words, all other points have a distance to `j` greater than or equal to `|i - j|`.

### Example:
Consider a set of points `{1, 3, 5, 8}`:
- For point `1`, the closest point is `3`.
- For point `3`, the closest points are both `1` and `5`.
- For point `5`, the closest point is `3`.
- For point `8`, the closest point is `5`.

### Objective:
Determine if it is possible to add a new integer point to the set such that:
- It is different from every existing point in the set.
- It becomes the closest point to every point in the set.

## Input Format
- The first line contains one integer `t` (1 ≤ t ≤ 1000) — the number of test cases.
- Each test case consists of two lines:
  - The first line contains one integer `n` (2 ≤ n ≤ 40) — the number of points in the set.
  - The second line contains `n` integers `x1, x2, ..., xn` (1 ≤ x1 < x2 < ... < xn ≤ 100) — the points from the set.

## Output Format
- For each test case, print `YES` if it is possible to add a new point according to the conditions. Otherwise, print `NO`.

## Constraints
- `1 ≤ t ≤ 1000`
- `2 ≤ n ≤ 40`
- `1 ≤ x1 < x2 < ... < xn ≤ 100`

## Example
```
### Input:
3
2
3 8
2
5 6
6
1 2 3 4 5 10

### Output:
YES
NO
NO
```


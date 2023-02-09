"""
An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform
a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color), and so on. Replace the color of all of the
aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""


from typing import List


def floodFillV1Recursive(
    image: List[List[int]], sr: int, sc: int, newColor: int
) -> List[List[int]]:
    R, C = len(image), len(image[0])
    color = image[sr][sc]

    if color == newColor:
        return image

    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < R:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < C:
                dfs(r, c + 1)

    dfs(sr, sc)
    return image


def floodFillV2Iterative(
    image: List[List[int]], sr: int, sc: int, newColor: int
) -> List[List[int]]:
    R, C = len(image), len(image[0])
    color = image[sr][sc]

    if color == newColor:
        return image

    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        image[r][c] = newColor
        if r >= 1 and image[r - 1][c] == color:
            stack.append((r - 1, c))
        if r + 1 < R and image[r + 1][c] == color:
            stack.append((r + 1, c))
        if c >= 1 and image[r][c - 1] == color:
            stack.append((r, c - 1))
        if c + 1 < C and image[r][c + 1] == color:
            stack.append((r, c + 1))

    return image

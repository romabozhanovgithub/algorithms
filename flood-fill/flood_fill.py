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
    # Get the number of rows and columns in the image
    R, C = len(image), len(image[0])
    # Store the color of the starting pixel
    color = image[sr][sc]

    # Return the original image if the starting color is the same as the new color
    if color == newColor:
        return image

    # Define a recursive function to perform the DFS
    def dfs(r, c):
        # If the color of the current pixel is the same as the starting color, update it to the new color
        if image[r][c] == color:
            image[r][c] = newColor
            # Check the up, down, left, and right pixels and perform DFS on them
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < R:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < C:
                dfs(r, c + 1)

    # Call the DFS function starting from the given starting pixel
    dfs(sr, sc)

    # Return the modified image
    return image


def floodFillV2Iterative(
    image: List[List[int]], sr: int, sc: int, newColor: int
) -> List[List[int]]:
    # Get the number of rows and columns in the image
    R, C = len(image), len(image[0])

    # Store the color of the starting pixel
    color = image[sr][sc]

    # Return the original image if the starting color is the
    # same as the new color
    if color == newColor:
        return image

    # Create a stack to store the pixels to be processed
    stack = [(sr, sc)]

    # Continue the loop until the stack is empty
    while stack:
        # Get the current pixel to be processed
        r, c = stack.pop()
        # Update the color of the current pixel to the new color
        image[r][c] = newColor

        # Check the up, down, left, and right pixels
        # If the color of a neighboring pixel is the same as the starting
        # color, add it to the stack
        if r >= 1 and image[r - 1][c] == color:
            stack.append((r - 1, c))
        if r + 1 < R and image[r + 1][c] == color:
            stack.append((r + 1, c))
        if c >= 1 and image[r][c - 1] == color:
            stack.append((r, c - 1))
        if c + 1 < C and image[r][c + 1] == color:
            stack.append((r, c + 1))

    # Return the modified image
    return image

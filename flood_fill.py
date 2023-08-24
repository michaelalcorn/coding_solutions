"""
FLOOD FILL 

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

"""

class Solution(object):

    def fill(self, image, sr, sc, from_color, to_color):
        if sr < 0 or sr >= len(image): return
        if sc < 0 or sc >= len(image[0]): return

        # change to to_color if it is the from_color
        if image[sr][sc] != from_color or image[sr][sc] == to_color: 
            return
        else: 
            image[sr][sc] = to_color

        # call fill on neighboring boxes
        self.fill(image, sr+1, sc, from_color, to_color)
        self.fill(image, sr-1, sc, from_color, to_color)
        self.fill(image, sr, sc+1, from_color, to_color)
        self.fill(image, sr, sc-1, from_color, to_color)

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        from_color = image[sr][sc]
        self.fill(image, sr, sc, from_color, color)
        return image

    
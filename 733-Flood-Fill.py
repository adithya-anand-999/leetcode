class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]

        if startColor == color:
            return image

        def help(r,c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            if image[r][c] != startColor:
                print(1)
                return 
            image[r][c] = color

            help(r+1,c)
            help(r-1,c)
            help(r,c+1)
            help(r,c-1)
        help(sr,sc)
        return image

        
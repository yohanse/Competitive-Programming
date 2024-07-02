class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_with_color = {}
        color_with_ball = {}
        query_length = len(queries)

        result = [0 for i in range(query_length)]
        distinct_color = 0
        for i in range(query_length):
            x, y = queries[i]
            if ball_with_color.get(x, 0):
                color = ball_with_color[x]
                color_with_ball[color] -= 1
                if color_with_ball[color] == 0:
                    distinct_color -= 1

            ball_with_color[x] = y
            color_with_ball[y] = color_with_ball.get(y, 0) + 1
            if color_with_ball[y] == 1:
                distinct_color += 1

            
            result[i] = distinct_color
        return result

        
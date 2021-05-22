"""
베스트 엘범

1) use hash function to count the total number of play for each genre
2) get the genre order using dictionary sorting by value
3) add song index up to 2 for each ganre by the number of play
"""


def solution(genres, plays):
    answer = []
    if len(genres) == 1:
        return [0]

    play_count = {}
    genres_idx = {}
    for i in range(len(genres)):
        if genres[i] in play_count:
            play_count[genres[i]] += plays[i]
        else:
            play_count[genres[i]] = plays[i]

        if genres[i] in genres_idx:
            genres_idx[genres[i]].append((i, plays[i]))
        else:
            genres_idx[genres[i]] = [(i, plays[i])]

    # dictionary sorting by value
    play_count = sorted(play_count.items(), key=lambda x: x[1], reverse=True)
    genres_order = [x for x, c in play_count]

    for g in genres_order:
        temp = genres_idx[g]
        temp = sorted(temp, key=lambda x: x[1], reverse=True)
        if len(temp) < 2:
            answer.append(temp[0][0])
        else:
            answer.extend([x for x, c in temp[:2]])

    return answer
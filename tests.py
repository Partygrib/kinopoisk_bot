from main.methods import search_film


def test_search():
    film = "her"
    correct0 = ["Her", "2020", "https://www.rottentomatoes.com/m/her_2020"]
    correct1 = ["Her", "2013", "https://www.rottentomatoes.com/m/her"]
    correct2 = ["Heropanti-2", "2022", "https://www.rottentomatoes.com/m/heropanti_2"]

    search = search_film(film)

    for i in 0, 1, 2:
        assert search[0][i] == correct0[i]
        assert search[1][i] == correct1[i]
        assert search[2][i] == correct2[i]


test_search()

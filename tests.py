from main.methods import search_film, search_full, search_pic


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


def test_pick_info():
    film = "her"
    correct0 = ["2020, Documentary, 42m", "Отсутствует информация", "Отсутствует информация", "", "Juan Carlos Borrero",
                "Melodie Carli"]
    phrase0 = "Отсутствует информация"
    correct1 = ["2013, Comedy/Drama, 1h 59m", "82", "94", "", "Spike Jonze"]
    phrase1 = "Sweet, soulful, and smart, Spike Jonze's Her uses its just-barely-sci-fi scenario to impart wryly funny wisdom about the state of modern human relationships."

    search = search_film(film)
    url1 = search[1][2]
    info1 = search_full(url1)

    for i in 0, 1, 2:
        assert info1[i] == correct1[i]

    assert info1[3].__contains__(phrase1)
    assert info1[4].__contains__(correct1[4])

    url0 = search[0][2]
    info0 = search_full(url0)

    for i in 0, 1, 2:
        assert info0[i] == correct0[i]

    assert info0[3].__contains__(phrase0)
    assert info0[4].__contains__(correct0[4])
    assert info0[4].__contains__(correct0[5])


test_pick_info()


def test_poster():
    film = "matrix"
    search = search_film(film)
    url1 = search[0][2]
    url2 = search[2][2]
    poster1 = search_pic(url1)
    poster2 = search_pic(url2)
    correct1 = "https://resizing.flixster.com/q1aWnhA588SmGiAht_9L3KXFUMA=/206x305/v2/https://flxt.tmsimg.com/assets/p22804_p_v8_av.jpg"
    notFound = "Постер отсутствует"

    assert poster1 == correct1
    assert poster2 == notFound


test_poster()

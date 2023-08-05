from indexnow import IndexNow


def test_initialize():
    index_now = IndexNow(key="57e85df435cd43bb", host="example.com")

    status = index_now.index(["https://www.example.com"])

    assert status == 200

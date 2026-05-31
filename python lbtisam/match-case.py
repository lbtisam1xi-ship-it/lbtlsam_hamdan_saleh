code = int(input("Enter HTTP status code: "))

match code:
    case 200 | 201 | 204:
        print("Success")

    case 301 | 302:
        print("Redirect")

    case 400:
        print("Bad Request")

    case 401:
        print("Unauthorized")

    case 404:
        print("Not Found")

    case c if 400 <= c < 500:
        print("Other Client Error")

    case c if 500 <= c < 600:
        print("Server Error")

    case _:
        print("Unknown Status")
import httpx

def request(url):
    try:
        response = httpx.get(
            url,
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except httpx.TimeoutException:
        print("Connection Timed Out")
    except httpx.ConnectError:
        print("Could not connect to server")
    except httpx.HTTPStatusError as e:
        print("Status Code: ", e.response.status_code)
        print("URL: ", e.request.url)
    except httpx.RequestError as e:
        print("Request Failure: ", e)
    except ValueError as e:
        print("Invalid Json Response")

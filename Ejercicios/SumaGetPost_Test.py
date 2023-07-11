import requests
import unittest

URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

A = 3
B = 2

parametros = {
    "a": A,
    "b": B
}

#def llamada(parametros):
#    response = requests.get(URL, params=parametros)

#    print(response.text)

#    if float(response.text) != 5:
#        raise AssertionError()

#    data = {
#        "a": A,
#        "b": B
#    }

#    response = requests.post(URL, json=data)

#    print(response.json()["result"])

#    if float(response.json()["result"]) != 5:
#        raise AssertionError()


class TestLlamada(unittest.TestCase):
    def test_request_get(self):

        parametros = {
            "a": A,
            "b": B
        }
        response = requests.get(URL, params=parametros)
        self.assertEqual(float(response.text), 5.0)

    def test_request_post(self):
        parametros = {
            "a": A,
            "b": B
        }
        response = requests.post(URL, params=parametros)
        self.assertEqual(float(response.json()["result"]), 5.0)

if __name__ == '__main__':
    unittest.main()
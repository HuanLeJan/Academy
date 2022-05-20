import requests
import xmltodict as xdc
from unittest import TestCase


class TestApi(TestCase):
    api = 'https://api.openweathermap.org/data/2.5/weather?'
    val_json = '{"coord"'
    json_len = len(val_json)
    val_xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml_len = len(val_xml)
    val_html = "<!DOCTYPE html>"
    html_len = len(val_html)

    def test_1_1(self):
        data = {"lat": "53.25", "lon": "15", "appid": ""}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 401)

    def test_1_2(self):
        data = {"lat": "53.25", "lon": "15", "appid": "pogodoweAPI"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 401)

    def test_1_3(self):
        data = {"lat": "53.25", "lon": "15", "appid": "3125897423784632"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 401)

    def test_1_4(self):
        data = {"lat": "53.25", "lon": "15", "appid": "3125897ds32d3d4556gs421s"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 401)

    def test_1_5(self):
        data = {"lat": "53.25", "lon": "15", "appid": "DROP DATABASE"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 401)

    def test_1_6(self):
        data = {"lat": "53.25", "lon": "15", "appid": "467d1ddbb26a41a94c1f3d3fbe27cc7e"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 200)

    def test_1_7(self):
        data = {"lat": "53.25", "lon": "15", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 200)

    def test_2_1(self):
        data = {"lat": "53,42659972319854", "lon": "14,5520208248849", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        print(api_call.text)
        api_body = api_call.json()
        self.assertEqual(api_body['name'], 'Szczecin')

    def test_2_2(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body['name'], 'Szczecin')

    def test_2_3(self):
        data = {"lat": "53,42659972319854", "lon": "14.5520208248849", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body['name'], 'Szczecin')

    def test_2_4(self):
        data = {"lat": "53.42659972319854", "lon": "374.551741", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_2_5(self):
        data = {"lat": "90.9854", "lon": "14,5520208248849", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_2_6(self):
        data = {"lat": "90.9854", "lon": "374.551741", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_2_7(self):
        data1 = {"lat": "", "lon": "14.5520208248849", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call1 = requests.get(TestApi.api, data1)
        print(api_call1.text)
        self.assertEqual(api_call1.status_code, 400)

    def test_2_8(self):
        data = {"lat": "55.532423", "lon": "", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_2_9(self):
        data2 = {"lat": "", "lon": "", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call1 = requests.get(TestApi.api, data2)
        print(api_call1.text)
        self.assertEqual(api_call1.status_code, 400)

    def test_2_11_0(self):
        data = {"lat": "ddsds", "lon": "32.32", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_2_12_1(self):
        data = {"lat": "    533232323.42659972319854   ", "lon": " 132324.5520208248849",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_2_13_2(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849  ", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_3_1(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "units": "", "mode": "xml",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        xml_to_dict = xdc.parse(api_call.text)
        self.assertEqual(xml_to_dict['current']['temperature']['@unit'], 'kelvin')

    def test_3_2(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "units": "standard", "mode": "xml",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        xml_to_dict = xdc.parse(api_call.text)
        self.assertEqual(xml_to_dict['current']['temperature']['@unit'], 'kelvin')

    def test_3_3(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "units": "metric", "mode": "xml",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        xml_to_dict = xdc.parse(api_call.text)
        self.assertEqual(xml_to_dict['current']['temperature']['@unit'], 'celsius')

    def test_3_4(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "units": "imperial", "mode": "xml",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        xml_to_dict = xdc.parse(api_call.text)
        self.assertEqual(xml_to_dict['current']['temperature']['@unit'], 'fahrenheit')

    def test_3_5(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "units": " metric", "mode": "xml",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        xml_to_dict = xdc.parse(api_call.text)
        self.assertEqual(xml_to_dict['current']['temperature']['@unit'], 'kelvin')

    def test_3_6(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "units": "METRIC", "mode": "xml",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        xml_to_dict = xdc.parse(api_call.text)
        self.assertEqual(xml_to_dict['current']['temperature']['@unit'], 'celsius')

    def test_3_7(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "units": "celcius", "mode": "xml",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        xml_to_dict = xdc.parse(api_call.text)
        self.assertEqual(xml_to_dict['current']['temperature']['@unit'], 'kelvin')

    def test_4_1(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849", "units": "celcius",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.json_len], TestApi.val_json)

    def test_4_2(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849",
                "mode": "", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.json_len], TestApi.val_json)

    def test_4_3(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849",
                "mode": "json", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.json_len], TestApi.val_json)

    def test_4_4(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849",
                "mode": "JSON", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.json_len], TestApi.val_json)

    def test_4_5(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849",
                "mode": "xml", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.xml_len], TestApi.val_xml)

    def test_4_6(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849",
                "mode": "XML", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.xml_len], TestApi.val_xml)

    def test_4_7(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849",
                "mode": "html", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.html_len], TestApi.val_html)

    def test_4_8(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849",
                "mode": "HTML", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.html_len], TestApi.val_html)

    def test_4_9(self):
        data = {"lat": "53.42659972319854", "lon": "14.5520208248849",
                "mode": "mina", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.text[:TestApi.json_len], TestApi.val_json)

    def test_5_1(self):
        data = {"lat": "51.10788524435801", "lon": "17.036626574495788",
                "lan": "pl", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], 'Wrocław')

    def test_5_2(self):
        data = {"lat": "51.10788524435801", "lon": "17.036626574495788",
                "lang": "de", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], 'Breslau')

    def test_5_3(self):
        data = {"lat": "51.10788524435801", "lon": "17.036626574495788",
                "lang": "DE", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], 'Breslau')

    def test_5_4(self):
        data = {"lat": "51.10788524435801", "lon": "17.036626574495788",
                "lan": " de", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], 'Wrocław')

    def test_5_5(self):
        data = {"lat": "51.10788524435801", "lon": "17.036626574495788",
                "lan": "polok", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], 'Wrocław')

    def test_5_6(self):
        data = {"lat": "51.10788524435801", "lon": "17.036626574495788",
                "lan": "", "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], 'Wrocław')

    def test_5_7(self):
        data = {"lat": "51.10788524435801", "lon": "17.036626574495788",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], 'Wrocław')

    def test_6_1(self):
        data = {"zip": ""
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_6_2(self):
        data = {"zip": "36117"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Montgomery")

    def test_6_3(self):
        data = {"zip": "73-110"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 404)

    def test_6_4(self):
        data = {"zip": "70-005,pl"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Szczecin")

    def test_6_5(self):
        data = {"zip": ","
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 400)

    def test_6_6(self):
        data = {"zip": "50-102,", "lat": "51.10788524435801", "lon": "17.036626574495788"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 404)

    def test_6_7(self):
        data = {"zip": "50-102,pl", "lat": "56.10788524435801", "lon": "25.036626574495788"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Wrocław")

    def test_6_8(self):
        data = {"zip": "36117,us", "mode": "xml", "lang": "pl",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = xdc.parse(api_call.text)
        self.assertEqual(api_body["current"]["city"]["@name"], "Montgomery")
        self.assertEqual(api_call.text[:TestApi.xml_len], TestApi.val_xml)

    def test_7_1(self):
        data = {"q": "Warsaw"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        print(api_body)
        self.assertEqual(api_body["name"], "Warsaw")

    def test_7_2(self):
        data = {"q": "Warszawa"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Warsaw")

    def test_7_3(self):
        data = {"q": "Warszawa,pl"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Warsaw")

    def test_7_4(self):
        data = {"q": "Warszawa,pol"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Warsaw")

    def test_7_5(self):
        data = {"q": "Warszawa,de"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        self.assertEqual(api_call.status_code, 404)

    def test_7_6(self):
        data = {"q": "Wrocław"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Wrocław")

    def test_7_7(self):
        data = {"q": "Las Vegas,nv,"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Las Vegas")

    def test_7_8(self):
        data = {"q": "Las Vegas,nv"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Las Vegas")

    def test_7_9(self):
        data = {"q": "Las Vegas,,us"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Las Vegas")

    def test_7_1_0(self):
        data = {"q": "Las Vegas,nv,us"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Las Vegas")

    def test_7_1_4(self):
        data = {"q": ",WA,us"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Aberdeen")

    def test_7_1_5(self):
        data = {"q": ",WA,us", "lat": "47.59411425613159", "lon": "-122.32812885713224"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Aberdeen")

    def test_7_1_6(self):
        data = {"lat": "47.59411425613159", "lon": "-122.32812885713224", "q": ",WA,us",
                "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Aberdeen")

    def test_7_1_7(self):
        data = {"q": "Aberdeen,WA,us"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Aberdeen")

    def test_7_1_8(self):
        data = {"zip": "36117,us", "q": "Aberdeen,WA,us"
            , "appid": "467D1DDBB26A41A94C1F3D3FBE27CC7E"}
        api_call = requests.get(TestApi.api, data)
        api_body = api_call.json()
        self.assertEqual(api_body["name"], "Aberdeen")

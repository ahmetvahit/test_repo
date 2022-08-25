import json
import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime


class crawl(scrapy.Spider):
    name = "Hepsiburada"
    output = []
    headers = {
        'cookie': '_gcl_au=1.1.591549031.1660413452; _gid=GA1.2.1359170139.1660413454; hbus_anonymousId=1fc07a1a-6c79-499c-ab2a-28455d520a37; _tt_enable_cookie=1; _ttp=aaec7b4f-e629-4ebc-bbe6-c43911581ebc; cookieconsentanon=false%7C13.08.2022%2020%3A57%3A40; cto_bundle=di2ecl9kSGo5UUtjWVZYOHlLbk1wUlNtanRKdlRUQTZYUnA3WUZ6MmdkYmNsb25QRzJobGhYSU95cE0zYTA4ZXpvSlRwdERPOTRoblQlMkJCTll1V2kwVm83bU5xU0V6UmNaOUgxTkp3YlU1WFhXc3FMODJhODkzZ0RsbCUyQk5jVmJuYzY3dVdmaWIyRkJMekFFOWthYVRYVnBGcE1BJTNEJTNE; _hjSessionUser_216130=eyJpZCI6IjJmZTBhMDc5LWQ1MGMtNTc1Yi1iZmY0LWVlMmQ2Yjk0MmJhNyIsImNyZWF0ZWQiOjE2NjA0MTM0NjA2NDMsImV4aXN0aW5nIjp0cnVlfQ==; dgr_searchresults=4175746f46696c7465724e657756616c69646174696f6e56347c64656661756c747c5573654e6577546f6c6b69656e50726564696374696f6e733d64697361626c65; isGlobalIp=1; _abck=BCEFE56ACBAB66E9FB8D719449E08536~0~YAAQjdlraDqco1yCAQAAj32Fmwjsqy6huSST2lfyIP98gZZ4rvQrxpNuporZjdoRRozrDATSDbTMNEVpcvzUL0X4zQkl0p1ldicSHJQY4S/woZF7a9NGFBXWYXT95gSr8GkxhMJvdlxE35UnkVUXMOIcysskW2xUyCWsScYpiWELRbpZc7BJy7xS2ySYCP53WD2CB6j2ZIYm8s2gYwS95jCVtTfy2gQ2OcND9pnQhB82Syq4QNkOqQgirSvHsS/CQNW+JmIiYOnPI32gCe3BlSn3hMS/jOoTBYmEkqlJfomdfQaBxC3p0JOffJgoj2ZN1UcZSVNBIBNQ5Zy7pfXSfdJmjJymXcbKCy0jwjPQg99y4qdYyy7fU9uU+GIz540noa2sK1keT3o5xmzQBdeRNQncGQc1PWSu7g9b/bE=~-1~-1~-1; bm_sz=E9BE16E347AC1CD9711ADA04F047628E~YAAQjdlraDuco1yCAQAAj32FmxCDqAk9JGsO8QCr9d9O14fb6JZpXPdTMOAdwW04wIiVKth+3Fz6Wt4d6zEOa2xRxmrGvWjSuKrcWVWbq2eP8qpycpjRy/TmSY4WAbor2O9HmoK85i4u7wsFlSpHh3rRIz30MdY7GIApXqI+rwgOOOAbEa6A5cmI+W/IC2FLr2flzVKUwzMovGB2wPPDLfhQa8aJafRv/5g3+YLtIZVaMOCek3sMm4omjaax81H++mNt5ZGtkPYb/Jbwf5MwiX4R+SVthOLTzTw6zROaEy/cmcjrbzTAxw==~3618373~3159602; wt3_eid=%3B289941511384204%7C2166041346800004667%232166046659000719809; wt3_sid=%3B289941511384204; _ga=GA1.2.1374688111.1660413454; _dc_gtm_UA-834379-1=1; ab.storage.sessionId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%228323f778-5247-2489-00af-05a32f6354fb%22%2C%22e%22%3A1660468391986%2C%22c%22%3A1660466591986%2C%22l%22%3A1660466591986%7D; ab.storage.deviceId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%22109b04d0-6f15-4090-5850-b64f3d886e15%22%2C%22c%22%3A1660413456413%2C%22l%22%3A1660466591988%7D; ab.storage.userId.a19ee87d-6625-49ed-ad8c-f427b0067dec=%7B%22g%22%3A%221fc07a1a-6c79-499c-ab2a-28455d520a37%22%2C%22c%22%3A1660413470228%2C%22l%22%3A1660466591988%7D; _hjIncludedInSessionSample=0; _hjSession_216130=eyJpZCI6ImUyNzM4NTM1LTYwMWItNDUzYy1iZGVlLTcxM2ZhZTVlOTM5ZSIsImNyZWF0ZWQiOjE2NjA0NjY2MDczMjUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _ga_44CSPTX731=GS1.1.1660466590.2.1.1660466611.39; hbus_sessionId=0ffde65d-87a8-4dea-985e-ebd9b2ff1cec%7C1660468428355',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = "https://www.hepsiburada.com/magaza"
    today = datetime.now().strftime("%Y-%m-%d")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    custom_settings = {
        "DOWNLOAD_DELAY": 0.2,
        "CONCURRENT_REQUESTS": 100,
        "RETRY_ENABLED": True,
        "RETRY_TIMES": 3
    }

    @staticmethod
    def prepare_urls():
        data = open("data/links_Hepsiburada.json", encoding="utf-8").read()
        data = json.loads(data)
        urls = []
        for row in data:
            urls.append(row)

        urls = list(set(urls))
        return urls

    def start_requests(self):
        urls = self.prepare_urls()
        for url in urls:
            full_link = f"{url}?siralama=coksatan"
            req = scrapy.Request(full_link, callback=self.continues, headers=self.headers)
            req.cb_kwargs["url"] = url
            yield req

    def continues(self, response, **kwargs):
        url = kwargs["url"]

        slug = url.split("/")[4]
        infos = response.xpath("//div[@class='merchant-information']/div/div/script/text()").get().strip()
        try:
            kep2 = [i.split("kep")[1].replace('":"', '').replace('","', '') for i in infos.split("mersisNumber")[:1]][0]
            kep = kep2 + 'kep.tr'
        except:
            kep = None
        try:
            mersis = \
                [i.split("mersisNumber")[1].replace('":"', '').replace('","', '') for i in
                 infos.split("merchantType")[:1]][
                    0]
        except:
            mersis = None

        phone = ''

        try:
            city = [i.split("city")[1].replace('":"', '').replace('","', '') for i in infos.split("profession")[:1]]
            m_city = city[0].capitalize()
        except:
            m_city = None
        try:
            name = [i.split("legalName")[1].replace('":"', '').replace('","', '') for i in infos.split("tagList")[:1]]
            m_name = name[0].capitalize()
            try:
                name2 = [i.split("nameAndSurname")[1].replace('":"', '').replace('","', '') for i in
                         infos.split("legalName")[:1]]
                m_name = name2[0].capitalize()
            except:
                pass
        except:
            m_name = None

        # Her satıcıdan bi ürün sepete ekleneceği için her satıcının en çok satanlar sayfasından ilk ürün linkini kaydettik
        urls = response.xpath("//div[@class='box product  hb-placeholder']/a/@href").getall()

        detail_url = f"https://www.hepsiburada.com{urls[0]}"

        req = scrapy.Request(detail_url, callback=self.parse, headers=self.headers)

        # req.cb_kwargs["slug"] = slug
        # req.cb_kwargs["kep"] = kep
        # req.cb_kwargs["mersis"] = mersis
        # req.cb_kwargs["m_city"] = m_city
        # req.cb_kwargs["brand"] = brand
        yield req
        self.output.append({
            "merchant_slug": slug,
            "m_name": m_name,
            "email": kep,
            "mersis_no": mersis,
            "phone": 'none',
            "city": m_city,
            "p_url": detail_url
        })

    def parse(self, response, **kwargs):  # TODO Ürün sayfasındasın!!
        pass

    def close(self, spider, reason):
        with open(f"data/step_4_merchant_company_details_{self.name}.json", "w", encoding="utf-8") as f:
            json.dump(self.output, f, ensure_ascii=False)

            # df = pd.read_json(json.dumps(self.output, ensure_ascii=False), encoding="utf-8")
            # df.to_excel("sample.xlsx",encoding="utf-8", index=False)


process = CrawlerProcess()
process.crawl(crawl)
process.start()

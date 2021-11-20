import scrapy


class Item(scrapy.Item):
    TAF  = scrapy.Field()
    METAR = scrapy.Field()
    sunrise = scrapy.Field()
    sundown = scrapy.Field()
    cartas = scrapy.Field()

class AISWebSpider(scrapy.Spider):
    name = 'minimal'
 
    def __init__(self, category=None, *args, **kwargs):
        super(AISWebSpider, self).__init__(*args, **kwargs)
        self.start_url = category
 
    def start_requests(self):
        return [scrapy.Request(self.start_url)]
 
    def parse(self, response):
        TAF = response.xpath("//h5[text()='TAF']/following-sibling::p/text()").extract() 
        METAR = [response.xpath("//h5[text()='METAR']/following-sibling::p/text()")[0].extract()] 
        sunrise = response.xpath("//sunrise/text()").extract()
        sundown = response.xpath("//sunset/text()").extract()
        names = response.xpath("//a[@title='Uso Ostensivo']/text()").extract()
        links = response.xpath("//a[@title='Uso Ostensivo']/@href").extract()
        cartas = []
        for i in range(0,len(names)):
            cartas.append({ 'name' : names[i],'link' : links[i]})
        
        yield Item(TAF = TAF, 
                      METAR = METAR, 
                      sunrise= sunrise, 
                      sundown=sundown,
                      cartas = cartas
                      )


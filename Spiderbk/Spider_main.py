from Spiderbk import URL_manager, HTML_downloader, HTML_parser, HTML_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = URL_manager.UrlManager()
        self.downloader = HTML_downloader.HtmlDownloader()
        self.parser = HTML_parser.HtmlParser()
        self.outputer = HTML_outputer.HtmlOutputer()
        
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('craw %d : %s') % (count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 1000:
                    break
                
                count = count + 1
            except:
                print 'craw failed'
        
        
        self.outputer.output_html()
    

if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
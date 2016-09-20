# coding: utf-8

class Person(object):
    def __init__(self, web_site):
        self.web = web_site

    def update_web(self, site):
        self.web = site
        return self.web

class LaoQi(Person):
    def update_web(self, site, lang="python"):
        self.web = site
        self.lang = lang
        return self.web, self.lang
    
    def about_me(self, name, site):
        my_web, my_lang = self.update_web(site)
        return {"name":name, "web":my_web, "lang":my_lang}


if __name__ == "__main__":
    #my = Person("www.itdiffer.com")
    my = LaoQi("www.itdiffer.com")
    print my.about_me("qiwsir", "qiwsir.github.io")

#output:
#{'lang': 'python', 'web': 'qiwsir.github.io', 'name': 'qiwsir'}

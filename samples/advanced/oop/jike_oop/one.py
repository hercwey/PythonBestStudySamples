# coding: utf-8

class Person(object):
    def __init__(self, web_site):
        self.web = web_site

    def update_web(self, site):
        self.web = site
        return self.web
    
class LaoQi(Person):
    def about_me(self, name, site):
        my_web = self.update_web(site)
        return {"name":name, "web":my_web}


if __name__ == "__main__":
    #my = Person("www.itdiffer.com")
    my = LaoQi("www.itdiffer.com")
    print my.about_me("qiwsir", "qiwsir.github.io")
    print my.web

#output:
#{'web': 'qiwsir.github.io', 'name': 'qiwsir'}
#qiwsir.github.io


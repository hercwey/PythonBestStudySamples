# coding: utf-8

class Person(object):
    def __init__(self, web_site):
        self.web = web_site

    def update_web(self, site):
        self.web = site
        return self.web

class LaoQi(Person):
    def __init__(self, teacher, web_site):
        self.teacher = teacher
        Person.__init__(self, web_site)    #unbound method
        #super(LaoQi,self).__init__(web_site)
        
    def update_web(self, site, lang="python"):
        self.web = site
        self.lang = lang
        return self.web, self.lang

    def your_teacher(self):
        return self.teacher
    
    def about_me(self, name, site):
        my_web, my_lang = self.update_web(site)
        return {"name":name, "web":my_web, "lang":my_lang}


if __name__ == "__main__":
    #my = Person("www.itdiffer.com")
    my = LaoQi("canglaoshi", "www.jikexueyuan.com")
    print my.your_teacher()
    print my.teacher
    print my.web

#canglaoshi
#canglaoshi
#www.jikexueyuan.com

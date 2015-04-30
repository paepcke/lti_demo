'''
Created on Apr 29, 2015

@author: paepcke
'''
import tornado.ioloop
import tornado.web

class LTIDillProvider(tornado.web.RequestHandler):
    '''
    classdocs
    '''

    def post(self):
        postBodyForm = self.request.arguments
        #print(str(postBody))
        self.echoParmsToBrowser(postBodyForm)

    def echoParmsToBrowser(self, postBodyForm):
        paramNames = postBodyForm.keys()
        paramNames.sort()
        self.write('<html><body>')
        self.write('<b>Dill Module Was Invoked With Parameters:</b><br><br>')
        for key in paramNames:
            self.write('<b>%s: </b>%s<br>' % (key, postBodyForm[key]))
        self.write("</body></html>")
        
    @classmethod  
    def makeApp(self):
        application = tornado.web.Application([
            (r"/dill", LTIDillProvider),
            ])
        return application

if __name__ == "__main__":
    application = LTIDillProvider.makeApp() 
    application.listen(7070)
    tornado.ioloop.IOLoop.instance().start()        
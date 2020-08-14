import requests
import json

class client:

    def __init__(self, serverUrl, port):
        # token,user
        self.token=''
        self.user=''
        self.serverUrl=serverUrl
        self.port=port
        self.api=serverUrl+":"+str(self.port)
        
    def register(self,name,email,password,organization):
        self.name=name
        self.email=email
        self.password=password
        self.organization=organization
        self.register_route = "/user/register"
        creds = {"name":self.name,"email": self.email,"password":self.password,"organization":self.organization}
        try:
         self.res = requests.post(self.api+self.register_route, json =creds)
        except:
          return self.parseResponse(408,"Connection Error")
        #return self.res.status_code, self.res.text
        return self.parseResponse(self.res.status_code,self.res.text)
                      
    def login(self,email,password):
        self.email=email
        self.password=password
        self.login_route =  "/user/login"
        creds = {"email": self.email,"password":self.password}
        try:
          self.res = requests.post(self.api+self.login_route, json =creds)
        except:
          return self.parseResponse(408,"Connection Error")

        return self.parseResponse(self.res.status_code,self.res.text)
        
        
    def parseResponse(self,status_code,res):
      if status_code == 200 :
          self.resData=json.loads(res)
          if "token" in res:
              self.token=self.resData['token']
              self.user=self.resData['user']
              return self.resData['message'],status_code
          else:
              return self.resData['message'],status_code
      elif status_code == 400:
        self.error=json.loads(res)['message']
        return self.error,status_code
      else :
        self.error= res
        return self.error,status_code
     
    #ToDO : implement custom Msgs for failed login
    def customResMsg(self,status,msg):
        if(status == 200 and "registered" in msg) :
           return "Registered!"
        if(status == 200 and "logged" in msg) :
           return "Logged in successfully"
        elif(status == 500 and "unique" in msg) :
          return "User Already Exists"
        elif(status == 500 and "required" in msg) :
          return  "Missing parameter"
     
     
#we will save token,user in a global variables to be used within all program
#token=''
#user=''
#client=client('http://192.168.1.39',3500)
#client.register('heroko','hero@test.me','heroko','org2')
#client.login('hero@test.me','heroko')
#print client.register('heroko3','hero3@test.me','heroko3','org3')
#print len(token) > 0 and len(user) > 0     
#print token , user
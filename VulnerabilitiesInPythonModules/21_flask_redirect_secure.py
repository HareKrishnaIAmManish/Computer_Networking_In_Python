from flask import Flask,redirect,Response
app=Flask(__name__)
#below is a whitelist
valid_locations=['www.packtpub.com','valid_url']
@app.route('/redirect/<url>')
def redirect_url(url):
    sanitizedLocation=getSanitizedLocation(url)#secure
    print(sanitizedLocation)
    return redirect("http://"+sanitizedLocation,code=302)
    #return redirect("http://www.domain.com/",code=302) #insecure
def getSanitizedLocation(location):
    if(location in valid_locations):
        return location
    else:
        return "check url"
if __name__=='__main__':
    app.run(debug=True)
    
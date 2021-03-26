a = 5

def run(folder,port=6540,host='0.0.0.0'):
    import os
    import shutil

    def copydirectorykut(src, dst):
        os.chdir(dst)
        list=os.listdir(src)
        nom= src+'.txt'
        fitx= open(nom, 'w')

        for item in list:
            fitx.write("%s\n" % item)

        fitx.close()

        f = open(nom,'r')
        for line in f.readlines():
            if "." in line:
                shutil.copy(src+'/'+line[:-1],dst+'/'+line[:-1])
            else:
                if not os.path.exists(dst+'/'+line[:-1]):
                    os.makedirs(dst+'/'+line[:-1])
                    copydirectorykut(src+'/'+line[:-1],dst+'/'+line[:-1])
                copydirectorykut(src+'/'+line[:-1],dst+'/'+line[:-1])
        f.close()
        os.remove(nom)
        os.chdir('..')
    copydirectorykut(folder,'/Users/toby/Library/Python/3.8/lib/python/site-packages/static_web/templates')
    from flask import Flask,render_template,redirect
    app = Flask('__main__')
    @app.route('/<file>/')
    def file(file):
        return render_template(file,files=os.listdir(folder))
    @app.route('/')
    def index():
        return redirect('/index.html/')
    app.run(port=port,host=host)
    
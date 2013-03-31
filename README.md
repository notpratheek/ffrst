weird name, ffrst ?

```sh
Commit time: Mon Apr  1 03:17:51 2013 +0530
```
Not a lot of creative folder names during that time !
(anyway it actually stands for, **f**lask **f**lask_flatpages **rst** )

---

Here's how to get started :
(actually I'll write it as code. As its much easier to understand !)

```sh
~ $ git clone https://github.com/Pychimp/ffrst.git
Cloning into 'ffrst'...
<clones the repo>


$ cd ffrst 
~/ffrst $ 


~/ffrst $ virtualenv .
New python executable in ./bin/python
Installing setuptools............done.
Installing pip...............done.


~/ffrst $ ls -Fa
./   bin/   .gitignore  journal/  README.md
../  .git/  include/    lib/      requirements.txt


~/ffrst $ source bin/activate
(ffrst) ~/ffrst $ 


(ffrst) ~/ffrst $ pip install -r requirements.txt
Downloading/unpacking <...downloads and install all packages from requirements.txt>
# Might wanna go and grab a cup of coffee ! :)
# docutils kinda freezes the process ! :|


(ffrst) ~/ffrst $ cd journal/
(ffrst) ~/ffrst/journal $ 

 
(ffrst) ~/ffrst/journal $ ls -Fa
./  ../  app.py  pages/  settings.py  utils.py


(ffrst) ~/ffrst/journal $ python app.py
# Fingers crossed ! If all goes well, then you should get this
* Running on http://127.0.0.1:8000/
* Restarting with reloader

```

open your browser and point it to http://127.0.0.1:8000/ (You should be greeted by Hello World !)
and just for kicks, try pointing to http://127.0.0.1:8000/hello-world/ (Should show some text ! 
Which is the HTML-ified version of [hello-world.rst](https://raw.github.com/Pychimp/ffrst/master/journal/pages/hello-world.rst))

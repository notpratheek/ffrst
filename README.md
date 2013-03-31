weird name, ffrst ?

```sh
Commit time: Mon Apr  1 03:17:51 2013 +0530
```
Not a lot of creative folder names during that time !
(anyway it actually stands for, **f**lask **f**lask_flatpages **rst** )

---

Here's how to get started :
(actuall I'll write it as code, much better to understand !)

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
./   bin/    .git/       include/  lib/
../  build/  .gitignore  journal/  requirements.txt


~/ffrst $ source bin/activate
(ffrst) ~/ffrst $ 


(ffrst) ~/ffrst $ pip install -r requirements.txt
Downloading/unpacking <...downloads and install all packages from requirements.txt>
# Might wanna go and grab a cup of coffee ! :)


(ffrst) ~/ffrst $ cd journal/
(ffrst) ~/ffrst/journal $ 

 
(ffrst) ~/ffrst/journal $ ls -Fa
./  ../  app.py  pages/  settings.py  utils.py


(ffrst) ~/ffrst/journal $ python app.py
# Fingers crossed ! If all goes well, then you should get this
* Running on http://127.0.0.1:8000/
* Restarting with reloader


```

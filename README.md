# GitLab Docker
private docker-compose

require
- ubuntu :16.*, 18.*

## initialize container
1. install require packages from base repo
<pre>
pip install -r requirements.txt
</pre>

1. clone modpy repository
- clone python helper scripts
<pre>
git clone http://10.120.41.10:8080/git/sakai.ko/modpy.git sh/modpy
</pre>

1. install require packages from helper repo
<pre>
pip install -r sh/modpy/requirements.txt
</pre>

1. generate container.
<pre>
sudo python3 ./init_container.py
</pre>

1. to install modules in container
<pre>
docker exec -it {container-name} python3 /tmp/sh/init.py
</pre>

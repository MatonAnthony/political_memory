Deployment on OpenShift
~~~~~~~~~~~~~~~~~~~~~~~

OpenShift is an Open-Source Platform-as-a-Service software by Red Hat. It is
also available in its hosted version known as "OpenShift Online" and the first
three websites ("gears") are free.

To deploy the website, use a command like::

    rhc app-create \
        postgresql-9.2 \
        python-2.7 \
        "http://cartreflect-claytondev.rhcloud.com/reflect?github=smarterclayton/openshift-redis-cart" \
        cron-1.4 \
        -n yourdomain \
        -a yourappname \
        -e DJANGO_SECRET_KEY=$(openssl rand -base64 32) \
        -e OPENSHIFT_PYTHON_WSGI_APPLICATION=memopol/wsgi.py \
        --from-code https://github.com/political-memory/political_memory.git

Then, either wait for the daily cron to fill up the database, either ssh into
the container and run the import commands manually.

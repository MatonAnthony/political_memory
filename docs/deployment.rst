Deployment on OpenShift
~~~~~~~~~~~~~~~~~~~~~~~

OpenShift is an Open-Source Platform-as-a-Service software by Red Hat. It is
also available in its hosted version known as "OpenShift Online" and the first
three websites ("gears") are free.

To deploy the website, use a command like::

    rhc app-create \
        python-2.7 \
        "http://cartreflect-claytondev.rhcloud.com/reflect?github=smarterclayton/openshift-redis-cart" \
        cron-1.4 \
        -n yourdomain \
        -a yourappname \
        -e DJANGO_SECRET_KEY=$(openssl rand -base64 32) \
        -e OPENSHIFT_PYTHON_WSGI_APPLICATION=memopol/wsgi.py \
        --from-code https://github.com/political-memory/political_memory.git \
        --deployment-branch yourbranch

.. danger:: Do not have any postgresql cartridge in your gear if you're on a
            free plan, since you won't have enough disk space to download the
            data and run the import scripts ! If you don't have a free plan,
            the only solution for now is to upload an sqlite database.

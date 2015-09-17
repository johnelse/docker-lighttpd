FROM                        ubuntu:14.04
MAINTAINER                  John Else <john.else@gmail.com>

RUN     apt-get update
RUN     apt-get -y install lighttpd

COPY    files/lighttpd.conf /etc/lighttpd/lighttpd.conf

VOLUME  ["/var/www"]

EXPOSE  8080

RUN     chown -R www-data /var/log/lighttpd
RUN     touch /var/run/lighttpd.pid
RUN     chown www-data /var/run/lighttpd.pid

USER    www-data

CMD     ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]

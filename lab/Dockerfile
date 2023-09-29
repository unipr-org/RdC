FROM ubuntu/nginx
RUN apt update
RUN apt install -y nmap tcpdump iptables curl net-tools whois traceroute tshark
RUN apt install -y openssh-server iputils-ping dnsutils nano
RUN echo -n ubuntu:ubuntu | chpasswd
RUN sed -i '2i /etc/init.d/ssh start' /docker-entrypoint.sh
EXPOSE 22

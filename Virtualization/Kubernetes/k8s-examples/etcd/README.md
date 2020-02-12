- pgrep etcd

- ps axf | grep advertise-client-urls
  - 11989 ?        Ssl    0:57      |   \_ etcd --advertise-client-urls=https://127.0.0.1:2379 --cert-file=/etc/kubernetes/pki/etcd/server.crt --client-cert-auth=true --data-dir=/var/lib/etcd --initial-advertise-peer-urls=https://127.0.0.1:2380 --initial-cluster=master=https://127.0.0.1:2380 --key-file=/etc/kubernetes/pki/etcd/server.key --listen-client-urls=https://127.0.0.1:2379 --listen-peer-urls=https://127.0.0.1:2380 --name=master --peer-cert-file=/etc/kubernetes/pki/etcd/peer.crt --peer-client-cert-auth=true --peer-key-file=/etc/kubernetes/pki/etcd/peer.key --peer-trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt --snapshot-count=10000 --trusted-ca-file=/etc/kubernetes/pki/etcd/ca.crt

- $ ps -T -p 11900
  PID  SPID TTY          TIME CMD
11900 11900 ?        01:28:12 etcd
11900 12012 ?        02:18:58 etcd
11900 12013 ?        01:24:48 etcd
11900 12014 ?        00:00:00 etcd
11900 12015 ?        00:00:00 etcd
11900 12016 ?        01:29:48 etcd
11900 12068 ?        01:29:45 etcd
11900 12105 ?        01:13:23 etcd
11900 12109 ?        01:27:53 etcd
11900 12141 ?        01:07:24 etcd
11900 24544 ?        00:42:59 etcd

- pstree -l -S -s -p 11900

- pstree -H 11989

```
  systemd─┬─accounts-daemon─┬─{gdbus}
          │                 └─{gmain}
          ├─acpid
          ├─2*[agetty]
          ├─atd
          ├─cron
          ├─dbus-daemon
          ├─dhclient
          ├─dockerd─┬─docker-containe─┬─7*[docker-containe─┬─pause]
          │         │                 │                    └─9*[{docker-containe}]]
          │         │                 ├─docker-containe─┬─kube-controller───8*[{kube-controller}]
          │         │                 │                 └─8*[{docker-containe}]
          │         │                 ├─docker-containe─┬─kube-scheduler───9*[{kube-scheduler}]
          │         │                 │                 └─8*[{docker-containe}]
          │         │                 ├─docker-containe─┬─kube-apiserver───10*[{kube-apiserver}]
          │         │                 │                 └─8*[{docker-containe}]
          │         │                 ├─docker-containe─┬─etcd───9*[{etcd}]
          │         │                 │                 └─9*[{docker-containe}]
          │         │                 ├─2*[docker-containe─┬─pause]
          │         │                 │                    └─8*[{docker-containe}]]
          │         │                 ├─docker-containe─┬─kube-proxy───7*[{kube-proxy}]
          │         │                 │                 └─8*[{docker-containe}]
          │         │                 ├─docker-containe─┬─runsvdir─┬─runsv───calico-felix───12*[{calico-felix}]
          │         │                 │                 │          ├─runsv───bird
          │         │                 │                 │          ├─runsv───confd───9*[{confd}]
          │         │                 │                 │          └─runsv───bird6
          │         │                 │                 └─9*[{docker-containe}]
          │         │                 ├─docker-containe─┬─install-cni.sh───sleep
          │         │                 │                 └─8*[{docker-containe}]
                    │         │                 │                 └─8*[{docker-containe}]
          │         │                 ├─docker-containe─┬─coredns───9*[{coredns}]
          │         │                 │                 └─8*[{docker-containe}]
          │         │                 ├─docker-containe─┬─coredns───10*[{coredns}]
          │         │                 │                 └─9*[{docker-containe}]
          │         │                 ├─docker-containe─┬─metrics-server───7*[{metrics-server}]
          │         │                 │                 └─9*[{docker-containe}]
          │         │                 └─27*[{docker-containe}]
          │         └─49*[{dockerd}]

```

- ./etcd --listen-client-urls=http://$IP1:2379, http://$IP2:2379, http://$IP3:2379, http://$IP4:2379, http://$IP5:2379 --advertise-client-urls=http://$IP1:2379, http://$IP2:2379, http://$IP3:2379, http://$IP4:2379, http://$IP5:2379

- kubectl -n kube-system get pod -o wide -l component=etcd
```
  NAME          READY     STATUS    RESTARTS   AGE       IP             NODE
  etcd-master   1/1       Running   0          1h        172.16.1.110   master
```

- kubectl -n kube-system get pod -o wide -l tier=control-plane
```
  NAME                             READY     STATUS    RESTARTS   AGE       IP             NODE
  etcd-master                      1/1       Running   0          1h        172.16.1.110   master
  kube-apiserver-master            1/1       Running   0          1h        172.16.1.110   master
  kube-controller-manager-master   1/1       Running   0          1h        172.16.1.110   master
  kube-scheduler-master            1/1       Running   0          1h        172.16.1.110   master
  ```

- kubectl -n kube-system exec etcd-master -it -- sh

- alias ctl8="ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key --cacert=/etc/kubernetes/pki/etcd/ca.crt"

- ctl8 check perf
```
   60 / 60 Booooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo! 100.00%1m0s
  PASS: Throughput is 151 writes/s
  PASS: Slowest request took 0.012149s
  PASS: Stddev is 0.000481s
  PASS
```


- ctl8 get --prefix --keys-only /
- ctl8 get --from-key --keys-only a

- ctl8 get --prefix /
- ctl8 get --prefix /registry
- ctl8 get --prefix --keys-only /registry/services

- Copy matching etcdctl binary from the etcd pod:
```
kubectl -n kube-system cp etcd-master:/usr/local/bin/etcdctl .
kubectl -n kube-system cp etcd-master:/usr/local/bin/etcdctl-3.2.18 .
chmod +x ./etcdctl
```

course = "Python \"Programming"
print(course)

course = "Python \nProgramming"
print(course)


first = "Mosh"
last = "Hamedani"
full_name = first + " " + last
full = f"{first} {last}"
print(full_name)
print(full)


x = 10
x += 3
print(x)


import math
print(math.ceil(2.1))

x = input("Enter a number: ")
y = int(x) + 1
print(f"x:{x},y:{y}")




{
  "log": {
    "loglevel": "warning"
  },
  "inbounds": [
    {
      "port": 1080,
      "listen": "127.0.0.1",
      "tag": "socks-inbound",
      "protocol": "socks",
      "settings": {
        "auth": "noauth",
        "udp": false,
        "ip": "127.0.0.1"
      },
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls"]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vless",
      "settings": {
        "vnext": [
          {
            "address": "your-server-address", // 服务器地址
            "port": 443, // 服务器端口
            "users": [
              {
                "id": "your-uuid", // 用户UUID
                "encryption": "none" // 必须设置为 none
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "tcp", // 根据您的需求选择 "tcp" 或 "ws"
        "security": "tls" // 如果使用TLS
      },
      "tag": "vless-out"
    },
    {
      "protocol": "freedom",
      "settings": {},
      "tag": "direct"
    },
    {
      "protocol": "blackhole",
      "settings": {},
      "tag": "blocked"
    }
  ],
  "routing": {
    "domainStrategy": "IPOnDemand",
    "rules": [
      {
        "type": "field",
        "outboundTag": "vless-out",
        "domain": ["geosite:cn"]
      },
      {
        "type": "field",
        "ip": ["geoip:private"],
        "outboundTag": "blocked"
      },
      {
        "type": "field",
        "domain": ["geosite:category-ads"],
        "outboundTag": "blocked"
      }
    ]
  },
  "dns": {
    "hosts": {
      "domain:v2fly.org": "www.vicemc.net",
      "domain:github.io": "pages.github.com",
      "domain:wikipedia.org": "www.wikimedia.org",
      "domain:shadowsocks.org": "electronicsrealm.com"
    },
    "servers": [
      "1.1.1.1",
      {
        "address": "114.114.114.114",
        "port": 53,
        "domains": ["geosite:cn"]
      },
      "8.8.8.8",
      "localhost"
    ]
  },
  "policy": {
    "levels": {
      "0": {
        "uplinkOnly": 0,
        "downlinkOnly": 0
      }
    },
    "system": {
      "statsInboundUplink": false,
      "statsInboundDownlink": false,
      "statsOutboundUplink": false,
      "statsOutboundDownlink": false
    }
  },
  "other": {}
}
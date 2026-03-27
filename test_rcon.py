from mcrcon import MCRcon

host = '192.168.1.42'
port = 25575
password = 'backup123'

try:
    with MCRcon(host, password, port=port) as mcr:
        print("✅ Connected to RCON!")
        response = mcr.command("say §a[Test] RCON is working from local machine!")
        print("✅ Message sent!")
except Exception as e:
    print(f"❌ Error: {e}")

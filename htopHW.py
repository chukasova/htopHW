import psutil

TEMPLATES = {
    "cpu": {
        "dev": "device disk: {device:_>10}, fstype disk: {fstype:_>10}",
        "maxfile": "maxfile count: {maxfile:_>8}, maxpath: {maxpath:_>13} "
    },
    "mem": {
        'total': "total memory   : {total:_>15}",
        'available': 'total available: {available:_>15}'
    }
}


def get_cpu_partitions():
    res = {"dev": [], "maxfile": []}
    data_partitions = psutil.disk_partitions(all=False)
    for cpu in data_partitions:
        res["dev"].append({"device": cpu.device, "fstype": cpu.fstype})
    data_partitions_maxfile = psutil.disk_partitions(all=False)
    for cpu in data_partitions_maxfile:
        res["maxfile"].append({"maxfile": cpu.maxfile, "maxpath": cpu.maxpath})
    return(res)


def get_memory():
    res = {}

    data_memory = psutil.virtual_memory()
    res['total'] = data_memory.total
    res['available'] = data_memory.available

    return res


def show(**kwargs):
    dev = kwargs["cpu"]["dev"]
    maxfile = kwargs["cpu"]["maxfile"]
    for d in dev:
        print(TEMPLATES["cpu"]["dev"].format(**d))
    for m in maxfile:
        print(TEMPLATES["cpu"]["maxfile"].format(**m))
    print('-'*48)
    print(TEMPLATES["mem"]['total'].format(**kwargs['mem']))
    print(TEMPLATES["mem"].get('available').format(**kwargs['mem']))


def main():
    cpu_info = get_cpu_partitions()
    info_mem = get_memory()
    show(cpu=cpu_info, mem=info_mem)


if __name__ == "__main__":
    main()

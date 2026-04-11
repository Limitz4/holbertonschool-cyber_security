#!/usr/bin/python3

import sys


def read_write_heap():
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    search_string = sys.argv[2].encode('ascii')
    replace_string = sys.argv[3].encode('ascii')

    if not search_string:
        sys.exit(1)

    maps_filename = f"/proc/{pid}/maps"
    mem_filename = f"/proc/{pid}/mem"

    heap_start = None
    heap_end = None

    try:
        with open(maps_filename, 'r') as f_maps:
            for line in f_maps:
                if '[heap]' in line:
                    parts = line.split()
                    addr_range = parts[0].split('-')
                    heap_start = int(addr_range[0], 16)
                    heap_end = int(addr_range[1], 16)
                    break
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if heap_start is None or heap_end is None:
        print("Error: Heap not found.")
        sys.exit(1)

    try:
        with open(mem_filename, 'rb+') as f_mem:
            f_mem.seek(heap_start)
            heap_data = f_mem.read(heap_end - heap_start)

            offset = heap_data.find(search_string)
            if offset == -1:
                print("Error: Search string not found in heap.")
                sys.exit(1)

            padded_replace = replace_string.ljust(len(search_string), b'\x00')

            f_mem.seek(heap_start + offset)
            f_mem.write(padded_replace)
            print(f"[{pid}] Replaced '{sys.argv[2]}' with '{sys.argv[3]}' at offset 0x{offset:x}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    read_write_heap()

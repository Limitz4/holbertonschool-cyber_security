    sys.exit(1)


def read_write_heap():
    """Ana fonksiyon: Heap b  lgesini tarar ve metni de ^=i ^=tirir."""
    # Arg  man kontrol  
    if len(sys.argv) != 4:
        print_usage_and_exit()

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit()

    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    if not search_string:
        return

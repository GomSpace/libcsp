#!/usr/bin/python

import sys
import os
import time
from libcsp import *

if __name__ == "__main__":

    # init csp
    csp_buffer_init(10, 300);
    csp_init(27);
    csp_zmqhub_init(27, "localhost")
    csp_rtable_set(7, 5, csp_zmqhub_if(), CSP_NODE_MAC)
    csp_route_start_task(1000, 0)
    time.sleep(1) # allow router startup
    csp_rtable_print()

    print("pinging addr 7, rc=" + str(csp_ping(7, 5000, 10)))

    # start listening for packets...
    sock = csp_socket()
    csp_bind(sock, 30)
    csp_listen(sock, 10)
    while True:
        conn = csp_accept(sock, 100)
        if not conn:
            continue

        while True:
            packet = csp_read(conn, 100)
            if not packet:
                break

            print("got packet, len=" + str(packet_length(packet)))

            csp_buffer_free(packet)
        csp_close(conn)


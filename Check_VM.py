import uuid
from datetime import datetime


# 8/13/2025
# Check VM mac Make Sure running on Real VM
# AUX-441


class check_VM:
    def check_vm_mac(self):
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                        for ele in range(0, 8 * 6, 8)][::-1])
        vm_macs = ["00:05:69", "00:0C:29", "00:1C:14", "00:50:56"]
        return any(mac.startswith(prefix) for prefix in vm_macs)

C = check_VM()
C.check_vm_mac()

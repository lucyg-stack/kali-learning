def interpret_bluetooth_class(cod_hex):
    # Convert hex to binary and strip '0b' prefix
    cod_bin = bin(int(cod_hex, 16))[2:].zfill(24)
    
    # Extracting bits for Major, Minor and Service classes
    major_class_bits = cod_bin[2:10]
    minor_class_bits = cod_bin[10:16]
    service_class_bits = cod_bin[16:24]
    
    # Convert binary to integer
    major_class = int(major_class_bits, 2)
    minor_class = int(minor_class_bits, 2)
    service_class = int(service_class_bits, 2)
    
    # Interpret Major Device Class
    major_class_dict = {
        0x00: "Miscellaneous",
        0x01: "Computer",
        0x02: "Phone",
        0x03: "Networking",
        0x04: "Audio/Video",
        0x05: "Peripheral",
        0x06: "Imaging",
        0x07: "Wearable",
        0x08: "Toy",
        0x09: "Health",
        0x0A: "Unused",
        0x0B: "Audio/Video (Headset)",
        0x0C: "Reserved"
    }
    
    # Interpret Minor Device Class (more details based on the major class)
    minor_class_dict = {
        0x00: "Unspecified",
        0x01: "Desktop workstation",
        0x02: "Server",
        0x03: "Laptop",
        0x04: "Handheld PC/PDA",
        0x05: "Phone",
        0x06: "Smartphone",
        0x07: "Tablet",
        0x08: "Wearable",
        0x09: "Media player",
        0x0A: "Gaming device",
        0x0B: "TV",
        0x0C: "Audio/Video equipment",
        0x0D: "Car",
        0x0E: "Health device",
        0x0F: "Unknown device"
        # You can add more based on the specific use cases
    }
    
    # Output the interpretation
    major_device = major_class_dict.get(major_class, "Unknown Major Class")
    minor_device = minor_class_dict.get(minor_class, "Unknown Minor Class")
    
    return {
        "Major Device Class": major_device,
        "Minor Device Class": minor_device,
        "Service Class": service_class
    }

# Input Class of Device
cod_input = input("Enter the Bluetooth Class of Device (e.g., 0x005a020c): ")
result = interpret_bluetooth_class(cod_input)

# Displaying the result
print("\nDevice Information:")
print(f"Major Device Class: {result['Major Device Class']}")
print(f"Minor Device Class: {result['Minor Device Class']}")
print(f"Service Class: {result['Service Class']}")


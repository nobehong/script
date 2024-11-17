def get_motherboard_type(serial_number, manufacture_year, has_hdmi):
    """
    Determines the Xbox 360 motherboard type based on the serial number,
    manufacture year, and HDMI port presence.
    """
    # Check based on serial number prefixes
    if serial_number.startswith("K"):
        return "Xenon"
    elif serial_number.startswith("L"):
        return "Zephyr"
    elif serial_number.startswith("M"):
        return "Falcon"
    elif serial_number.startswith("N"):
        return "Jasper"
    
    # Additional checks based on year and HDMI
    if 2005 <= manufacture_year <= 2006 and not has_hdmi:
        return "Xenon (based on year and no HDMI)"
    elif manufacture_year == 2007 and has_hdmi:
        return "Zephyr (first HDMI model)"
    elif 2007 <= manufacture_year <= 2008 and not has_hdmi:
        return "Falcon (improved thermals, no HDMI)"
    elif 2008 <= manufacture_year <= 2009 and has_hdmi:
        return "Jasper (smaller chip, HDMI included)"
    elif 2010 <= manufacture_year <= 2011 and has_hdmi:
        return "Trinity or Corona (slim models)"
    else:
        return "Unknown motherboard type"

def main():
    """
    Main function to interact with the user and determine the motherboard type.
    """
    # Get user inputs
    serial_number = input("Enter your Xbox 360 serial number: ").strip().upper()
    try:
        manufacture_year = int(input("Enter the manufacture year (e.g., 2005): ").strip())
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    
    hdmi_input = input("Does your console have an HDMI port? (yes/no): ").strip().lower()
    has_hdmi = hdmi_input == "yes"
    
    # Determine motherboard type
    motherboard_type = get_motherboard_type(serial_number, manufacture_year, has_hdmi)
    print(f"The motherboard type for your Xbox 360 is: {motherboard_type}")

if __name__ == "__main__":
    main()

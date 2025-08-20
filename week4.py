# File and Exception Handling

def modify_content(content):
    """
    This is an easy function that modifies the
    file content into uppercase letters
    """
    return content.upper()

def main():
    # Ask user for input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # try opening and reading the file
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # Modifying content
        modified_content = modify_content(content)

        # Creating a new output file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"Modified file written successfully as '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'.")
    

# Calling the main function for execution
if __name__ == "__main__":
    main()
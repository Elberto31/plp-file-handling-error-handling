def read_and_modify_file():
    try:
        # Ask the user for the filename to read
        input_filename = input("Enter the filename to read: ")

        # Try opening the input file
        with open(input_filename, "r") as infile:
            # Read the content of the file
            content = infile.read()

            # Modify the content (example: convert to uppercase)
            modified_content = content.upper()

            # Ask the user for the output filename
            output_filename = input("Enter the filename to write the modified content: ")

            # Write the modified content to the new file
            with open(output_filename, "w") as outfile:
                outfile.write(modified_content)

            print(f"File '{input_filename}' has been read and modified content written to '{output_filename}'.")
    
    except FileNotFoundError:
        print("Error: The file you entered does not exist. Please check the filename and try again.")
    except IOError as e:
        print(f"Error: An I/O error occurred while accessing the file. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()

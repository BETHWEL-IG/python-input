def read_and_write_file():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ").strip()
        
        # open and read the file
        with open(input_file, 'r') as file:
            content = file.readlines()
        
        # Process the content (modify it)
        modified_content = [line.upper() for line in content] 
        
        # Ask the user for the output file name
        output_file = input("Enter the name of the file to write to: ").strip()
        
        # Write the modified content to a new file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"File has been successfully written to {output_file}.")
    
    except FileNotFoundError:
        print("Error: The specified file does not exist. Please try again.")
    except IOError:
        print("Error: There was a problem reading or writing the file. Please check permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()

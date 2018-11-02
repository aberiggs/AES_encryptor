import os, random, sys, re, pkg_resources
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key, filename):
    chunk_size = 64 * 1024
    out_file = os.path.join(os.path.dirname(filename), "enc."+os.path.basename(filename))
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = ''
    
    print(out_file)

    for i in range(16):
        IV += chr(random.randint(0, 0xff))

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, "rb") as infile:
        with open(out_file, "wb") as outfile:
            outfile.write(file_size)
            outfile.write(IV)
            while True:
                chunk = infile.read(chunk_size)

                if len(chunk) == 0:
                    break

                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 -(len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
    rename_file = os.path.basename(filename)
    if rename_file.startswith("enc."):
        out_file_test = rename_file[4:]
        print(out_file_test)
    out_file = os.path.join(os.path.dirname(filename), out_file_test)
    chunksize = 64 * 1024
    with open(filename, "rb") as infile:
        filesize = infile.read(16)
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(out_file, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            
            outfile.truncate(int(filesize))
            print(out_file)
            print(out_file_test)
            


def allfiles():
    all_files = []
    for root, subfiles, files in os.walk(os.getcwd()):
        for names in files:
            all_files.append(os.path.join(root, names))

    return all_files


print("Press 1 to encypt all files in current directory")
print("Press 2 to decrypt all files in current directory")
print("Press 3 to decrypt only the selected file")
choice = raw_input("\nChoice: ")
password = raw_input("Enter the password: ")

enc_files = allfiles()

if choice == "1":
    for Tfiles in enc_files:
        if os.path.basename(Tfiles).startswith("enc."):
            print("%s is already encrypted" %str(Tfiles))
            pass

        elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
            pass
       
        else:
            encrypt(SHA256.new(password).digest(), str(Tfiles))
            print("Encryption Finished on %s" %str(Tfiles))
            os.remove(Tfiles)

elif choice == "2":
    for Tfiles in enc_files:
        if not os.path.basename(Tfiles).startswith("enc."):
            pass

        elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
            pass
       
        else:
            out_file = decrypt(SHA256.new(password).digest(), Tfiles)
            os.remove(Tfiles)

elif choice == "3":
    filename = raw_input("Enter the file to decrypt: ")
    if not os.path.exists(filename):
        print("The file does not exist")
        sys.exit(0)
   
    elif not filename.startswith("enc."):
       print("%s is not detected as needing decryption" %filename)
       sys.exit

    else:
        decrypt(SHA256.new(password).digest(), filename)
        print("Done decrypting %s" %filename)
        os.remove(filename)

else:
    print("Please choose a valid command")
    sys.exit()

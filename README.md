# Caesar_cypher
1. instatiate the Cypher() class and pass in the required arguements.
-the **text_path** is the path of the uploaded pdf document and "r" should be added before the path for it to be readable
-The **s** is the shift key for the encryption

2. To encrypt the uploaded pdf, call the encrypt method .encrypt()
3. To save the encrypted document as pdf call the .write_text_to_pdf() method and input the argument "output_pdf" to name your file and end it with ".pdf"
   for example, Note.write_text_to_pdf(output_pdf= "File_name.pdf")

4. Instantiate the Decrypt() class which inherits properties from the Cypher() class
   -pass in the path of the encrypted file into the arguemnet **text_path** and "r" should be added before the path for it to be readable
   example, Denote = Decrypt(text_path = r"file path")
5. To decrypt the uploaded pdf, call the decrypt method .decrypt()
6. To save the decrypted document as pdf call the .rewrite_text_to_pdf() method and input the argument "output_pdf" to name your file and end it with ".pdf"
   for example, Note.rewrite_text_to_pdf(output_pdf= "File_name.pdf")

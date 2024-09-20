#A python program to illustrate Caesar Cipher Technique
import pdfplumber
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



class Cypher :
    def __init__(self,text_path,s):
        # self.text = text
        self.text_path = text_path
        self.s = s

# A method to extract the text from the pdf
    def access_pdf(self):
        with pdfplumber.open(self.text_path) as pdf:
            all_text = ""
            for page in pdf.pages:
                # Extract text from each page
                all_text += page.extract_text()
                # print (all_text)
        return all_text

# A method to encrypt the text
    def encrypt(self):
        result = ""
         # traverse text
        text_extract = self.access_pdf()
        for i in range(len(text_extract)):
            char = text_extract[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + self.s-65) % 26 + 65)

            # Encrypt lowercase characters
            elif char.islower():
                result += chr((ord(char) + self.s - 97) % 26 + 97)

            # rturn anything other than alphabets
            else:
                result += char
        print (result)
        return result

# converts the encrypted file back to a pdf but the output_pdf element should be .pdf
    def write_text_to_pdf(self,output_pdf):
        text = self.encrypt()
        c = canvas.Canvas(output_pdf, pagesize=letter)
        width, height = letter
        c.setFont("Helvetica", 12)
        lines = text.split('\n')
        y = height - 40

        for line in lines:
            c.drawString(40, y, line)
            y -= 14

            if y < 40:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 40

        c.save()


# 2 Creating a new class for decryption
class Decrypt(Cypher):
    def decrypt(self):
        d_result = ""
         # traverse text
        text2_extract = self.access_pdf()
        for i in range(len(text2_extract)):
            char = text2_extract[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                d_result += chr((ord(char) - self.s - 65) % 26 + 65)

            # Encrypt lowercase characters
            elif char.islower():
                d_result += chr((ord(char) - self.s - 97) % 26 + 97)

            # return anything other than alphabets
            else:
                d_result += char
        print (d_result)
        return d_result

# converts the decrypted file back to a pdf but the output_pdf element should be .pdf
    def rewrite_text_to_pdf(self,output_pdf):
        text = self.decrypt()
        c = canvas.Canvas(output_pdf, pagesize=letter)
        width, height = letter
        c.setFont("Helvetica", 12)
        lines = text.split('\n')
        y = height - 40

        for line in lines:
            c.drawString(40, y, line)
            y -= 14

            if y < 40:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 40

        c.save()




First = Cypher(text_path=r"C:\Users\LONEWOLF\Documents\Graphite\Caesar_cypher\pump.pdf", s=3)
First.encrypt()
First.write_text_to_pdf(output_pdf="File1.pdf")
Second = Decrypt (text_path=r"C:\Users\LONEWOLF\Documents\Graphite\File1.pdf", s=3)
Second.decrypt()
Second.rewrite_text_to_pdf(output_pdf = "file3.pdf")
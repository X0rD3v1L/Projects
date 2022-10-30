import os,json

class HuffmanLetter:
        def __init__(self, HuffmanLetter, freq):
            self.HuffmanLetter = HuffmanLetter
            self.freq = freq

class HuffmanEnCoding:
    def __init__(self,path):
        self.path = path
        self.codes = {}
        self.reverseMapping = {}

    class HeapNode:
        def __init__(self,freq,leftChild,rightChild):
            self.freq = freq
            self.leftChild = leftChild
            self.rightChild = rightChild


    def makeFrequencyDict(self,text):
        counterDict = {}
        for character in text:
            counterDict[character] = counterDict[character] + 1 if character in counterDict.keys() else 1
        mapping = sorted([HuffmanLetter(c, f) for c, f in counterDict.items()], key=lambda l: l.freq)
        return mapping

    def buildHuffmanTree(self,frequency):
        while(len(frequency) > 1):
            leftChild = frequency.pop(0);
            rightChild = frequency.pop(0);
            totalFreq = leftChild.freq + rightChild.freq
            node = self.HeapNode(totalFreq,leftChild,rightChild);
            frequency.append(node)
            frequency.sort(key=lambda l:l.freq)
        return frequency[0]


    def assignCodes__helper(self,root,curCode):
        if(type(root) is HuffmanLetter):
            self.codes[root.HuffmanLetter] = curCode
            self.reverseMapping[curCode] = root.HuffmanLetter
            return
        self.assignCodes__helper(root.leftChild,curCode + "0")
        self.assignCodes__helper(root.rightChild,curCode + "1")

    def assignCodes(self,root):
        curCode = ""
        self.assignCodes__helper(root,curCode)

    def getEncodedText(self,text):
        encodedText = ""
        for character in text:
            encodedText += self.codes[character]
        return encodedText

    def padEncodedText(self,encodedText):
        extraPadding = 8 - (len(encodedText)) % 8
        for i in range(extraPadding):
            encodedText += "0"

        paddedInfo = "{0:08b}".format(extraPadding)
        encodedText = paddedInfo + encodedText
        return encodedText

    def getByteArray(self,paddedEncodedText):
        if (len(paddedEncodedText) % 8 != 0):
            exit(0)

        bArr = bytearray()
        for i in range(0,len(paddedEncodedText),8):
            byte = paddedEncodedText[i:i+8]
            bArr.append(int(byte,2))
        return bArr

    def compress(self):
        fileName,ext = os.path.splitext(self.path)
        outputPath = fileName + ".bin"

        with open(self.path,"r+") as file,open(outputPath,"wb") as output:
            text = file.read().rstrip()

            frequency = self.makeFrequencyDict(text)
            root = self.buildHuffmanTree(frequency)
            self.assignCodes(root)
            encodedText = self.getEncodedText(text)
            paddedEncodedText = self.padEncodedText(encodedText)
            b = self.getByteArray(paddedEncodedText)
            output.write(json.dumps(self.reverseMapping).encode('utf-8') + b'\n')
            output.write(bytes(b))

        return outputPath

    def removePadding(self,paddedEncodedText):
        paddedInfo = paddedEncodedText[:8]
        extraPadding = int(paddedInfo,2)

        padEncodedText = paddedEncodedText[8:]
        encodedText = padEncodedText[:-1*extraPadding]
        return encodedText

    def decodedText(self,encodedText):
        curCode = ""
        decodedText = ""
        for bit in encodedText:
            curCode += bit;
            if (curCode in self.reverseMapping):
                character = self.reverseMapping[curCode]
                decodedText += character
                curCode = ""
        return decodedText

    def decompress(self,inputPath):
        filename, file_extension = os.path.splitext(self.path)
        outputPath = filename + "_decompressed" + ".txt"

        with open(inputPath, 'rb') as file, open(outputPath, 'w') as output:
            bit_string = ""
            lines = next(file)
            mapping = json.loads(lines.decode('utf-8'))
            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.removePadding(bit_string)

            decompressed_text = self.decodedText(encoded_text)
            
            output.write(decompressed_text)

        return outputPath

# path = "/home/x0r_d3v1l/Desktop/MiniProject/english-lorem.txt"
# main = HuffmanEnCoding(path)
# comPath = main.compress()
# decomPath = main.decompress(comPath)
# print(decomPath)
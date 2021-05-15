import en_core_web_sm
nlp = en_core_web_sm.load()

class data_pipeline:

    def count_sents(self,text):
      x=0
      mytext = nlp(text)
      for sentence in mytext.sents: 
       x=x+1
      return x


    def calculate_average (self,text):
        lengthes =[]
        mytext = nlp(text)
        for sentence in mytext.sents:
                words = str(sentence).split()
                lengthes.append(len(words))
        average = sum(lengthes)/len(lengthes)
        return average 



    def list_sen(self,text):
         sents=[]
         mytext = nlp(text)
         for sentence in mytext.sents:
            sents.append(str(sentence))
         return sents 

    def list_sen(self,text):
        sents=[]
        mytext = nlp(text)
        for sentence in mytext.sents:
            sents.append(str(sentence))
        return sents

    def wh_parse_text (self,text):
         answers = [] 
         sents = self.list_sen(text)
         average = int(self.calculate_average(text))
         count = self.count_sents(text)
         step = int(80/average)
         for i in range(count):
             if (i % step == 0 and i+step < count):
              answers.append(" ".join(sents[i:i+step]))
         return answers

